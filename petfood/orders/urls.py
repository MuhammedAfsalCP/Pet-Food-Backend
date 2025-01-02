
from django.urls import path

from .views import OrderView,OrderUpdate


urlpatterns = [
     path('orderview/',OrderView.as_view()),
     path('orderupdate/<int:pk>',OrderUpdate.as_view())
    
]
