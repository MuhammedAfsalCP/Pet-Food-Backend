from django.shortcuts import render
from .serialzer import CartItemSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
# Create your views here.

class CartView(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer