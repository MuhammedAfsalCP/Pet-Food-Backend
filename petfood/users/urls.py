
from django.urls import path
from .views import UserDetails,Login
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/',UserDetails.as_view()),
    path('login/',Login.as_view()),
]




