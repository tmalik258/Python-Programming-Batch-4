from django.urls import path

from . import views

urlpatterns = [
    path('add_to_cart/<uuid:product_id>', views.addToCart, name='add-to-cart')
]