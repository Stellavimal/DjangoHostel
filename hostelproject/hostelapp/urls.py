# Inside hostelapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .models import *

router = DefaultRouter()
router.register(r'rooms', views.ModelViewSet)

# Add other viewsets and routes as needed

urlpatterns = [
    
    path('api/', include(router.urls)),
  
]
