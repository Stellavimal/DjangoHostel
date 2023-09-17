from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register('rooms',roomsViewSet)
router.register('roombooking',roombookingViewSet)


urlpatterns=[
    path('api/',include(router.urls)),
]