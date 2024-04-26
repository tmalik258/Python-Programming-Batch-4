from django.contrib import admin

from .models import Order, OrderItem


# for order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['city', 'country', 'zip_code', 'is_placed', 'is_canceled', 'status']


# for orderItem model
admin.site.register(OrderItem)