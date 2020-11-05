from django.urls import path, include
from . import views
from .views import *
from .datos import *


urlpatterns = [
    path('', views.Presentacion, name='Presentacion'),
    path('sala_administrador', views.sala_administrador, name='sala_administrador'),
    path('sala_registros', views.sala_registros, name='sala_registros'),
    path('sala_quejas', views.sala_quejas, name='sala_quejas'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),

    path('datos/', Datos.as_view(), name='datos'),
    path('ListData/', ListData.as_view(), name='ListData')

]