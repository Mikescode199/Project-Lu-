from django.db import models

# Create your models here.

CAUSAS = (
    (1, ("Enfermedad")),
    (2, ("Accidente")),
    (3, ("Nacimiento")),
    (4, ("A causa de mi trabajo/otros")),
)
class DatosUsuario(models.Model):
    graduacion_ojo_izquierdo = models.CharField(max_length=500)
    graduacion_ojo_derecho = models.CharField(max_length=500)
    edad_actual = models.IntegerField()
    edad_empezo_lentes = models.IntegerField()
    causa_uso_lentes = models.IntegerField(choices = CAUSAS, blank= True)

class QuejaSugerencias(models.Model):
    queja_sugerencia = models.TextField()