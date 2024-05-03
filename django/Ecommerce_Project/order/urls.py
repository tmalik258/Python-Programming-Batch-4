from django.urls import path

from . import views

urlpatterns = [
    path('add_to_cart/<uuid:product_id>', views.addToCart, name='add-to-cart'),
    path('subtract_from_cart/<uuid:product_id>', views.subtractFromCart, name='subtract-from-cart'),
    path('remove_from_cart/<int:order_item_id>', views.removeFromCart, name='remove-from-cart'),
    path('cart/', views.showCart, name='show-cart'),
    path('checkout/', views.checkout, name='checkout')
]