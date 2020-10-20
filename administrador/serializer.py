from django.urls import path, include
from .models import DatosUsuario
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosUsuario
        fields = '__all__'
