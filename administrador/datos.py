from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *


class Datos(APIView):
    authentication_classes =[]
    permission_classes = []

    def get(self, request, format=None):
        Enfermedad = DatosUsuario.objects.filter(causa_uso_lentes=1).count,
        Accidente = DatosUsuario.objects.filter(causa_uso_lentes=2).count,
        Nacimiento = DatosUsuario.objects.filter(causa_uso_lentes=3).count,
        trabajootros = DatosUsuario.objects.filter(causa_uso_lentes=4).count

        serializer = UserSerializer(Enfermedad)

        datos = {'Enfermedad' : Enfermedad,
                'Accidente' : Accidente,
                'Nacimiento' : Nacimiento,
                'trabajootros' : trabajootros
        }

        return Response(serializer.datos)