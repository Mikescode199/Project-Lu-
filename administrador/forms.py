from django import forms 
from . import views
from .models  import DatosUsuario

class LoginForm(forms.Form):
    #Con estas lineas de código podemos registrar a un usuario
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class FormularioUser(forms.ModelForm):
        class Meta: 
            model = DatosUsuario
            fields = [
                    'graduacion_ojo_izquierdo',
                    'graduacion_ojo_derecho',
                    'edad_actual',
                    'edad_empezo_lentes',

            ]

            labels = {
                    'graduacion_ojo_izquierdo' : 'Graduación ojo izquierdo',
                    'graduacion_ojo_derecho': 'Graduación ojo derecho',
                    'edad_actual': 'Edad actual',
                    'edad_empezo_lentes': 'Edad en la que comenzó a usar lentes',
            }

            widgets = {
                    'graduacion_ojo_izquierdo':forms.TextInput(attrs={'class':'form-input'}),
                    'graduacion_ojo_derecho' : forms.TextInput(attrs={'class':'form-input'}),
                    'edad_actual' : forms.TextInput(attrs={'class':'form-input'}),
                    'edad_empezo_lentes' : forms.TextInput(attrs={'class':'form-input'}),
            }
