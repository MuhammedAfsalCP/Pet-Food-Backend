from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_deleted=models.BooleanField(default=False)
    email=models.EmailField(unique=True)
    def createsuperuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
    
class Ingredients(models.Model):
    name=models.CharField(max_length=30)


class Products(models.Model):
    class CategoryChoices(models.TextChoices):
        NULL='NULL'
        DOG='Dog'
        CAT='Cat'

    Name=models.CharField(max_length=50)
    Category=models.CharField(max_length=4,choices=CategoryChoices.choices,default=CategoryChoices.NULL)
    Price=models.DecimalField(max_digits=7,decimal_places=2)
    Description=models.TextField()
    Brand=models.CharField(max_length=20)
    Weight=models.CharField(max_length=20)
    Stock=models.IntegerField()
    Ratin=models.DecimalField(max_digits=2,decimal_places=1)
    Image=models.ImageField(upload_to='products/')
    Ingredient=models.ManyToManyField(Ingredients)


    def __str__(self):
        return self.Name



