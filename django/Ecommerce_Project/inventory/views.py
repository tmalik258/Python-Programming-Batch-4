from django.shortcuts import render, HttpResponse

from .models import Product, Category

# Create your views here.


# This is landing page
def homeView(request):
    products = Product.objects.all()

    return render(request, 'inventory/index.html', {
        'products': products,
    })


# This is product detail page
def productDetailView(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, 'inventory/detail.html', {
        'product': product
    })


def productsListByCategoryView(request, category_slug):
    category_obj = Category.objects.get(slug=category_slug)

    products = Product.objects.filter(category=category_obj)

    return render(request, 'inventory/products_by_category.html', {
        'products': products,
        'category': category_obj
    })
