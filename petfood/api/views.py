from django.shortcuts import render
# from .serializer import UserRegisterSerializer
from rest_framework.viewsets import ModelViewSet
from .models import User
# Create your views here.

# class UserDetails(ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserRegisterSerializer