# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils import timezone
# import uuid

# class User(AbstractUser):
#     ROLE_CHOICES = [
#         ('supplier', 'Supplier'),
#         ('buyer', 'Buyer'),
#         ('admin', 'Administrator'),
#     ]
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
#     phone = models.CharField(max_length=20, blank=True)

# class SupplierProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supplier_profile')
#     business_name = models.CharField(max_length=255)
#     business_address = models.TextField()
#     country = models.CharField(max_length=100)

# class BuyerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer_profile')
#     business_name = models.CharField(max_length=255)
#     shipping_address = models.TextField()
#     country = models.CharField(max_length=100)

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     CONDITION_GRADES = [
#         ('A', 'A - Excellent'),
#         ('B', 'B - Good'),
#         ('C', 'C - Fair'),
#         ('D', 'D - Poor'),
#     ]
#     supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE, related_name='products')
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     brand = models.CharField(max_length=100, blank=True)
#     size = models.CharField(max_length=50, blank=True)
#     condition_grade = models.CharField(max_length=1, choices=CONDITION_GRADES)
#     quantity = models.PositiveIntegerField(default=1)
#     unit_price = models.DecimalField(max_digits=12, decimal_places=2)
#     currency = models.CharField(max_length=3, default='USD')
#     image = models.ImageField(upload_to='products/', blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]
#     order_reference = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
#     buyer = models.ForeignKey(BuyerProfile, on_delete=models.PROTECT, related_name='orders')
#     supplier = models.ForeignKey(SupplierProfile, on_delete=models.PROTECT, related_name='orders')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     total_amount = models.DecimalField(max_digits=14, decimal_places=2)
#     currency = models.CharField(max_length=3, default='USD')
#     order_date = models.DateTimeField(default=timezone.now)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     quantity = models.PositiveIntegerField()
#     unit_price = models.DecimalField(max_digits=12, decimal_places=2)

# class CartItem(models.Model):
#     """Simple cart stored in DB for logged-in buyers"""
#     buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, related_name='cart_items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid

class User(AbstractUser):
    ROLE_CHOICES = [
        ('supplier', 'Supplier'),
        ('buyer', 'Buyer'),
        ('admin', 'Administrator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    phone = models.CharField(max_length=20, blank=True)

class SupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supplier_profile')
    business_name = models.CharField(max_length=255)
    business_address = models.TextField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name

class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer_profile')
    business_name = models.CharField(max_length=255)
    shipping_address = models.TextField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

class Product(models.Model):
    CONDITION_GRADES = [
        ('A', 'A - Excellent'),
        ('B', 'B - Good'),
        ('C', 'C - Fair'),
        ('D', 'D - Poor'),
    ]
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    condition_grade = models.CharField(max_length=1, choices=CONDITION_GRADES)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    order_reference = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.PROTECT, related_name='orders')
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.order_reference

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)

class CartItem(models.Model):
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)