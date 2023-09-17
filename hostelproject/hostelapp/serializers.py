from rest_framework import serializers
from .models import *

class roomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=rooms
        fields="__all__"
class roombookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=roombooking
        fields="__all__"
