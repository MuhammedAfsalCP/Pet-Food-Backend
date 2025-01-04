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
    
    def delete(self):
        self.is_delete=True
        self.is_active=False
        self.save()
    
