# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     # Supplier
#     path('products/', views.product_list, name='product_list'),
#     path('products/add/', views.product_add, name='product_add'),
#     path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
#     # Buyer
#     path('marketplace/', views.browse, name='browse'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('cart/', views.cart_view, name='cart'),
#     path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
#     path('checkout/', views.checkout, name='checkout'),
#     # Orders
#     path('orders/', views.order_list, name='order_list'),
#     path('orders/<int:pk>/', views.order_detail, name='order_detail'),
#     path('orders/<int:pk>/confirm/', views.order_confirm, name='order_confirm'),
#     path('orders/<int:pk>/ship/', views.order_ship, name='order_ship'),
#     path('orders/<int:pk>/deliver/', views.order_deliver, name='order_deliver'),
#     # Payment simulation
#     path('orders/<int:pk>/pay/', views.simulate_payment, name='simulate_payment'),
#     # Invoice
#     path('orders/<int:pk>/invoice/', views.generate_invoice, name='invoice'),
#     # Tracking
#     path('orders/<int:pk>/track/', views.tracking, name='tracking'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('marketplace/', views.browse, name='browse'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/confirm/', views.order_confirm, name='order_confirm'),
    path('orders/<int:pk>/ship/', views.order_ship, name='order_ship'),
    path('orders/<int:pk>/deliver/', views.order_deliver, name='order_deliver'),
    path('orders/<int:pk>/pay/', views.simulate_payment, name='simulate_payment'),
    path('orders/<int:pk>/invoice/', views.generate_invoice, name='invoice'),
    path('orders/<int:pk>/track/', views.tracking, name='tracking'),
]