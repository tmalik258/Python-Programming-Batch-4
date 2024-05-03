from django.db import models
from django.contrib.auth.models import User

from inventory.models import Product


# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('f', 'Fulfilled'),
        ('p', 'In Progress')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=300, blank=True, null=True)
    address_line_2 = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    is_placed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='p')


class OrderItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product_id.title} | {self.order_id.is_placed} | {self.quantity}"
    
    def total(self):
        price = 0
        if self.product_id.discounted_price:
            price = self.product_id.discounted_price
        else:
            price = self.product_id.price
        return price * self.quantity
