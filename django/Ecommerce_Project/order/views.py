from django.shortcuts import render, HttpResponse

from .models import Order, OrderItem

from inventory.models import Product
# Create your views here.

def addToCart (request, product_id):
    try:
        old_cart = Order.objects.get(is_placed=False)
        product_obj = Product.objects.get(pk=product_id)
        
        try:
            order_item_obj = old_cart.order_items.get(product_id=product_obj)
            order_item_obj.quantity = order_item_obj.quantity + 1
            order_item_obj.save()
        except OrderItem.DoesNotExist:
            new_order_item_obj = OrderItem(order_id=old_cart, product_id=product_obj, quantity=1)
            new_order_item_obj.save()

        return HttpResponse("Unplaced order Exists")
    except Order.DoesNotExist:
        new_cart = Order()
        new_cart.user = request.user
        new_cart.save()
        print('new order created')

        product_obj = Product.objects.get(pk=product_id)
        order_item_obj = OrderItem(order_id=new_cart, product_id=product_obj, quantity=1)
        order_item_obj.save()
        print('Product is added to cart')

        return HttpResponse('Order Created and product is added to that cart')
    