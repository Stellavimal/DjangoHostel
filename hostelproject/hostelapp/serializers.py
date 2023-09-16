from rest_framework import serializers
from .models import rooms

class roomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=rooms
        fields="__all__"
