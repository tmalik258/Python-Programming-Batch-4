from django.urls import path

from .views import homeView, productDetailView, productsListByCategoryView

urlpatterns = [
    path('', homeView, name='index'),
    path('products/<uuid:product_id>', productDetailView, name='product_detail'),
    path('search/<slug:category_slug>', productsListByCategoryView, name='products_list')
]