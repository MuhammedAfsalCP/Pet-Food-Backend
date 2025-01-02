from django.shortcuts import render
from .serializer import UserRegisterSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class UserDetails(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer

class Login(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
           
            return Response({
                'access': access_token,
                'refresh': str(refresh)
            })
        else:
            return Response('invalid User', status=status.HTTP_401_UNAUTHORIZED)