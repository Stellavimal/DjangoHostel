from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import roomsViewSet
from .views import RegisterViewSet


router = routers.DefaultRouter()
router.register('rooms', roomsViewSet)
router.register('Register',RegisterViewSet)






urlpatterns = [
    path('api/', include(router.urls)),
]