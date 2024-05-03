from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem
from .forms import AddressForm

from inventory.models import Product
# Create your views here.

@login_required
def addToCart (request, product_id):
    try:
        old_cart = Order.objects.get(user=request.user, is_placed=False)
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


@login_required
def subtractFromCart(request, product_id):
    try:
        order = Order.objects.get(is_placed=False, user=request.user)
        product_obj = Product.objects.get(pk=product_id)
 
        try:
            order_item_obj = order.order_items.get(product_id=product_obj)
            if order_item_obj.quantity > 1:
                order_item_obj.quantity = order_item_obj.quantity - 1
                order_item_obj.save()
            else:
                order_item_obj.delete()
 
            if order.order_items.count() == 0:
                order.delete()
 
            return redirect('show-cart')
 
        except OrderItem.DoesNotExist:
            return redirect('show-cart')
 
    except Order.DoesNotExist:
        return redirect('show-cart')


@login_required
def removeFromCart(request, order_item_id):
    order_item = OrderItem.objects.get(id=order_item_id)
    order = order_item.order_id
    order_item.delete()

    if order.order_items.count() == 0:
        order.delete()

    return redirect('show-cart') 


@login_required
def showCart(request):
    try:
        cart = Order.objects.get(user=request.user, is_placed=False)
        cart_items = cart.order_items.all()
        
        return render(request, 'order/cart.html', {
            'cart_items': cart_items
        })
    except Order.DoesNotExist:
        return render(request, 'order/cart.html')

@login_required
def checkout(request):
    try:
        order = Order.objects.get(is_placed=False, user=request.user)

        if request.method == 'POST':
            form = AddressForm(request.POST, instance=order)

            if form.is_valid():
                form_obj = form.save(commit=False)
                form_obj.is_placed = True
                form_obj.save()

                return redirect('index')
        else:
            form = AddressForm()   
        return render(request, 'order/checkout.html', {
            'form': form
        })

    except Order.DoesNotExist:
        return redirect('index')