from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('', views.Presentacion, name='Presentacion'),
    path('sala_administrador', views.sala_administrador, name='sala_administrador'),

]