from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.get_or_create_cart, name='get-or-create-cart'),
    path('cart/clear/', views.clear_cart, name='clear-cart'),
    path('cart/items/', views.list_cart_items, name='list-cart-items'),
    path('cart/items/add/', views.add_to_cart, name='add-to-cart'),
    path('cart/items/delete/<int:pk>/', views.delete_cart_item, name='delete-cart-item'),
]