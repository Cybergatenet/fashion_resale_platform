from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from .forms import ProductForm, RegistrationForm
import uuid
from xhtml2pdf import pisa
from django.template.loader import get_template

def index(request):
    return render(request, 'marketplace/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            if user.role == 'supplier':
                SupplierProfile.objects.create(user=user)
            else:
                BuyerProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'marketplace/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'marketplace/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    user = request.user
    ctx = {'user': user}
    if user.role == 'supplier':
        profile = getattr(user, 'supplier_profile', None)
        if not profile:
            return redirect('index')
        products = user.supplier_profile.products.filter(is_active=True).count()
        orders = user.supplier_profile.orders.exclude(status='cancelled').count()
        revenue = user.supplier_profile.orders.filter(status='completed').aggregate(
            total=models.Sum('total_amount'))['total'] or 0
        recent_orders = user.supplier_profile.orders.order_by('-order_date')[:5]
        ctx.update(profile=profile, products_count=products, orders_count=orders,
                   revenue=revenue, recent_orders=recent_orders)
    elif user.role == 'buyer':
        profile = getattr(user, 'buyer_profile', None)
        if not profile:
            return redirect('index')
        orders = user.buyer_profile.orders.exclude(status='cancelled').count()
        recent_orders = user.buyer_profile.orders.order_by('-order_date')[:5]
        ctx.update(profile=profile, orders_count=orders, recent_orders=recent_orders)
    return render(request, 'marketplace/dashboard.html', ctx)

# Supplier Product Management
@login_required
def product_list(request):
    if request.user.role != 'supplier':
        return redirect('browse')
    products = request.user.supplier_profile.products.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

@login_required
def product_add(request):
    if request.user.role != 'supplier':
        return redirect('browse')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = request.user.supplier_profile
            product.save()
            messages.success(request, 'Product listed')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'marketplace/product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    if request.user.role != 'supplier':
        return redirect('browse')
    product = get_object_or_404(Product, pk=pk, supplier=request.user.supplier_profile)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'marketplace/product_form.html', {'form': form})

# Buyer Marketplace
def browse(request):
    products = Product.objects.filter(is_active=True, quantity__gt=0).select_related('supplier__user', 'category')
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    grade = request.GET.get('grade')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if query:
        products = products.filter(title__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)
    if grade:
        products = products.filter(condition_grade=grade)
    if min_price:
        products = products.filter(unit_price__gte=min_price)
    if max_price:
        products = products.filter(unit_price__lte=max_price)

    categories = Category.objects.all()
    return render(request, 'marketplace/browse.html', {
        'products': products,
        'categories': categories,
        'grades': Product.CONDITION_GRADES
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'marketplace/product_detail.html', {'product': product})

# Cart
# @login_required
# def cart_view(request):
#     if request.user.role != 'buyer':
#         return redirect('browse')
#     items = request.user.buyer_profile.cart_items.select_related('product').all()
#     total = sum(item.product.unit_price * item.quantity for item in items)
#     return render(request, 'marketplace/cart.html', {'items': items, 'total': total})

@login_required
def cart_view(request):
    if request.user.role != 'buyer':
        return redirect('browse')
    cart_items = request.user.buyer_profile.cart_items.select_related('product').all()
    # Build a list with subtotal computed for each item
    items_with_subtotal = []
    total = 0
    for item in cart_items:
        subtotal = item.product.unit_price * item.quantity
        items_with_subtotal.append({
            'cart_item': item,
            'subtotal': subtotal,
        })
        total += subtotal
    return render(request, 'marketplace/cart.html', {
        'items': items_with_subtotal,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    if request.user.role != 'buyer':
        return redirect('browse')
    product = get_object_or_404(Product, pk=product_id, is_active=True)
    buyer = request.user.buyer_profile
    cart_item, created = CartItem.objects.get_or_create(buyer=buyer, product=product)
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(CartItem, pk=cart_id, buyer=request.user.buyer_profile)
    cart_item.delete()
    return redirect('cart')

@login_required
@transaction.atomic
def checkout(request):
    if request.user.role != 'buyer':
        return redirect('browse')
    buyer = request.user.buyer_profile
    cart_items = buyer.cart_items.select_related('product').all()
    if not cart_items:
        messages.error(request, 'Cart is empty')
        return redirect('cart')

    total = sum(item.product.unit_price * item.quantity for item in cart_items)
    supplier = cart_items[0].product.supplier

    # Create order
    order = Order.objects.create(
        buyer=buyer,
        supplier=supplier,
        total_amount=total,
        status='pending'
    )
    order.order_reference = f"ORD-{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
    order.save()

    for item in cart_items:
        product = item.product
        if product.quantity < item.quantity:
            messages.error(request, f'Not enough stock for {product.title}')
            return redirect('cart')
        product.quantity -= item.quantity
        product.save()
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item.quantity,
            unit_price=product.unit_price
        )

    cart_items.delete()
    return redirect('order_detail', pk=order.pk)

# Orders
@login_required
def order_list(request):
    user = request.user
    if user.role == 'supplier':
        orders = user.supplier_profile.orders.all().order_by('-order_date')
    elif user.role == 'buyer':
        orders = user.buyer_profile.orders.all().order_by('-order_date')
    else:
        orders = Order.objects.all().order_by('-order_date')
    return render(request, 'marketplace/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'marketplace/order_detail.html', {'order': order})

@login_required
def order_confirm(request, pk):
    order = get_object_or_404(Order, pk=pk, supplier=request.user.supplier_profile)
    if order.status == 'pending':
        order.status = 'confirmed'
        order.save()
    return redirect('order_detail', pk=order.pk)

@login_required
def order_ship(request, pk):
    order = get_object_or_404(Order, pk=pk, supplier=request.user.supplier_profile)
    if order.status == 'confirmed':
        order.status = 'shipped'
        order.save()
    return redirect('order_detail', pk=order.pk)

@login_required
def order_deliver(request, pk):
    order = get_object_or_404(Order, pk=pk, buyer=request.user.buyer_profile)
    if order.status == 'shipped':
        order.status = 'delivered'
        order.save()
    return redirect('order_detail', pk=order.pk)

# Payment simulator
@login_required
def simulate_payment(request, pk):
    order = get_object_or_404(Order, pk=pk, buyer=request.user.buyer_profile)
    if order.status == 'confirmed':
        if request.method == 'POST':
            # Simulate successful payment
            order.status = 'processing'
            order.save()
            messages.success(request, 'Payment successful! Order is now processing.')
            return redirect('order_detail', pk=order.pk)
        return render(request, 'marketplace/payment_simulator.html', {'order': order})
    return redirect('order_detail', pk=order.pk)

# Invoice PDF
# @login_required
# def generate_invoice(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     template = get_template('marketplace/invoice.html')
#     html = template.render({'order': order})
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="invoice_{order.order_reference}.pdf"'
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('PDF generation error')
#     return response

@login_required
def generate_invoice(request, pk):
    order = get_object_or_404(Order, pk=pk)
    # Compute subtotal for each order item
    for item in order.items.all():
        item.subtotal = item.unit_price * item.quantity
    template = get_template('marketplace/invoice.html')
    html = template.render({'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.order_reference}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation error')
    return response

# Shipment Tracking
def tracking(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'marketplace/tracking.html', {'order': order})