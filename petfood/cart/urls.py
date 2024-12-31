
from django.urls import path
from .views import CartAdd,CartDelete





urlpatterns = [
    path('cartadd/',CartAdd.as_view()),
    path('cartadd/<int:pk>/',CartDelete.as_view())
    
]
