from django.shortcuts import render
from .serialzer import CartItemSerializer,CartSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
# Create your views here.

class CartAdd(CreateAPIView,ListAPIView):
    serializer_class=CartItemSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self,serializer):
        user = self.request.user
        
        cart, created = Cart.objects.get_or_create(user=user)
        product = serializer.validated_data['product']
        quantity=serializer.validated_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity+=quantity
            cart_item.save()
            return Response('successfully added',status=status.HTTP_200_OK)
        serializer.save(cart=cart)

        return Response('successfully added',status=status.HTTP_201_CREATED)

    def get_queryset(self):
        # Get the cart items for the authenticated user
        user = self.request.user
        return CartItem.objects.filter(cart__user=user)

    def list(self, request, *args, **kwargs):
        # Override list method to return the cart items
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    

class CartDelete(APIView):
    def get(self,request,pk):
        try:
            cart_item=CartItem.objects.get(id=pk)
            serializer=CartItemSerializer(cart_item)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return Response('cart not found',status=status.HTTP_404_NOT_FOUND)
        


    def delete(self,request,pk):
        try:
            cart_item=CartItem.objects.get(id=pk)
            cart_item.delete()
            return Response('item Deleted',status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        
        try:
            action = request.data.get('method')
            if action=='increase':
                cart_item=CartItem.objects.get(id=pk)
                cart_item.quantity+=1
                cart_item.save()
                serializer=CartItemSerializer(cart_item)
            elif action=='decrease':
                cart_item=CartItem.objects.get(id=pk)
                if cart_item.quantity>0:
                    cart_item.quantity-=1
                    serializer=CartItemSerializer(cart_item)
            
            cart_item.save()
            return Response("updated",status=status.HTTP_200_OK)
        
        except:
            return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)



        

    
    
