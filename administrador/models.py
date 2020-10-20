from django.db import models

# Create your models here.

CAUSAS = (
    (1, ("Disease")),
    (2, ("Accidente")),
    (3, ("Accident")),
    (4, ("Because of my work / others")),
)
class DatosUsuario(models.Model):
    graduacion_ojo_izquierdo = models.CharField(max_length=10)
    graduacion_ojo_derecho = models.CharField(max_length=10)
    edad_actual = models.IntegerField()
    edad_empezo_lentes = models.IntegerField()
    causa_uso_lentes = models.IntegerField(choices = CAUSAS, blank= True)

class QuejaSugerencias(models.Model):
    queja_sugerencia = models.TextField()