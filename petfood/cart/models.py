from django.db import models
from users.models import User
from products.models import Products
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cartitems')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property

    def item_subtotal(self):
        return self.product.Price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.product} from {self.cart.user.username}'s Cart"