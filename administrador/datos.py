from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.views.generic import ListView

class Datos(ListView):
    def get(self, request, *args, **kwargs):
        
        data = {'Enfermedad' : DatosUsuario.objects.filter(causa_uso_lentes=1).count,
                'Accidente' : DatosUsuario.objects.filter(causa_uso_lentes=2).count,
                'Nacimiento' : DatosUsuario.objects.filter(causa_uso_lentes=3).count,
                'trabajootros' : DatosUsuario.objects.filter(causa_uso_lentes=4).count
        }
        return render(request, 'Data/data.html' , data)


class ListData(APIView):

    def get(self, request, format=None):

        causa = DatosUsuario.objects.all()
        # data = {'Enfermedad' : DatosUsuario.objects.filter(causa_uso_lentes=1).count,
        #         'Accidente' : DatosUsuario.objects.filter(causa_uso_lentes=2).count,
        #         'Nacimiento' : DatosUsuario.objects.filter(causa_uso_lentes=3).count,
        #         'trabajootros' : DatosUsuario.objects.filter(causa_uso_lentes=4).count
        # }
        serializer = UserSerializer(causa, many=True)
        return Response(serializer.data)