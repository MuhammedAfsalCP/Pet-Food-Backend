
from django.urls import path

from .views import OrederCreate


urlpatterns = [
     path('orderlist/',OrederCreate.as_view())
    
]
