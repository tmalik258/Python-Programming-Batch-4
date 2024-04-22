from django.urls import path

from .views import homeView, productDetailView, productsListView

urlpatterns = [
    path('', homeView, name='index'),
    path('products/<uuid:product_id>', productDetailView, name='product_detail'),
    path('search/<slug:category_slug>', productsListView, name='products_list')
]