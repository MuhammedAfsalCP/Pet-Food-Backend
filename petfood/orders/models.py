from django.db import models
from products.models import Products
from users.models import User
import uuid
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    address=models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'

class OrderItem(models.Model):
    class StatusChoices(models.TextChoices):
        ("SH", "Shipping"),
        ("CA", "Cancelled"),
        ("RT", "Returned"),
       
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    status=models.CharField(max_length=10,choices=StatusChoices.choices,default='SH')

    @property

    def item_subtotal(self):
        return self.product.Price * self.quantity

    
    def __str__(self):
        return f'{self.quantity} x {self.product.Name} in order {self.order.order_id}'