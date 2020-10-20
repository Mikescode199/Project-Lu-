from django import forms 
from . import views
from .models  import *
class LoginForm(forms.Form):
        #Con estas lineas de código podemos registrar a un usuario
        username = forms.CharField(widget=forms.TextInput())
        password = forms.CharField(widget=forms.PasswordInput())

        
class FormularioUser(forms.ModelForm):
        class Meta: 
                model = DatosUsuario
                fields = '__all__'
                
                labels = {
                        'graduacion_ojo_izquierdo' : 'Left eye graduation',
                        'graduacion_ojo_derecho': 'Right eye graduation',
                        'edad_actual': 'Edad actual',
                        'edad_empezo_lentes': 'Age you started wearing a lens',
                        'causa_uso_lentes' : 'Cause you started wearing glasses',
                }

                widgets = {
                        'graduacion_ojo_izquierdo':forms.TextInput(attrs={'class':'form-input'}),
                        'graduacion_ojo_derecho' : forms.TextInput(attrs={'class':'form-input'}),
                        'edad_actual' : forms.TextInput(attrs={'class':'form-input'}),
                        'edad_empezo_lentes' : forms.TextInput(attrs={'class':'form-input'}),
                }



class FormularioQueja_suegerencia(forms.ModelForm):
        class Meta: 
                model = QuejaSugerencias

                fields = '__all__'

                labels = {
                        'queja_sugerencia' : 'Add a complaint or suggestion',

                }

                widgets = {
                        'queja_sugerencia' : forms.TextInput(attrs={}),
                }