from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import roomsViewSet

router=routers.DefaultRouter()
router.register('rooms',roomsViewSet)


urlpatterns=[
    path('api/',include(router.urls)),
]