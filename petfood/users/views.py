from django.shortcuts import render
from .serializer import UserRegisterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import User
# Create your views here.
class UserDetails(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer