from django.db import models

# Create your models here.

class DatosUsuario(models.Model):
    graduacion_ojo_izquierdo = models.IntegerField()
    graduacion_ojo_derecho = models.IntegerField()
    edad_actual = models.IntegerField()
    edad_empezo_lentes = models.IntegerField()

