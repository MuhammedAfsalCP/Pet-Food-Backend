from django.db import models
from products.models import Products
from users.models import User
import uuid
# Create your models here.

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        ("SH", "Shipping"),
        ("OR", "Order Received"),
        ("CA", "Cancelled"),
        ("RT", "Returned"),
        ("RF", "Refunded"),
    products=models.ManyToManyField(Products,through='OrderItem',related_name='orders')
    order_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    address=models.TextField()
    status=models.CharField(max_length=10,choices=StatusChoices.choices,default='SH')

    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    @property

    def item_subtotal(self):
        return self.product.Price * self.quantity

    
    def __str__(self):
        return f'{self.quantity} x {self.product.Name} in order {self.order.order_id}'