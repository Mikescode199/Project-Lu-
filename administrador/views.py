from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def Presentacion(request):
    
    #FORMULARIO
    form_prueba_ojos = FormularioUser(request.POST or None)
    if request.method == 'POST':
        form_prueba_ojos = FormularioUser(request.POST or None)
        if form_prueba_ojos.is_valid():
            instance = form_prueba_ojos.save(commit=False)
            instance.user = request.user
            form_prueba_ojos.save()
            return redirect('Presentacion')
    else:
        pass

    #QUEJAS O SUGERENCIAS
    form_quejas_sugerencias = FormularioQueja_suegerencia(request.POST or None)
    if request.method == 'POST':
        form_quejas_sugerencias = FormularioQueja_suegerencia(request.POST or None)
        if form_quejas_sugerencias.is_valid():
            instance = form_quejas_sugerencias.save(commit=False)
            instance.user = request.user
            form_quejas_sugerencias.save()
            return redirect('Presentacion')
    else:
        pass
    #REGISTRO ////////////////////////////////////////////////////
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            print(user, password)
            user = authenticate(username= user, password = password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('sala_administrador')
                else:
                    pass
            else:
                pass
    context ={
        'form': form,
        'form_prueba_ojos' : form_prueba_ojos,
        'form_quejas_sugerencias' : form_quejas_sugerencias,
        }
    
    return render(request, 'Presentacion/index.html', context)


#Sala de administración
@login_required(login_url='/Presentacion')
def sala_administrador(request):
    
    registros_creados = DatosUsuario.objects.count()
    usuarios_registrados = User.objects.count()
    numero_quejas = QuejaSugerencias.objects.count()


    context ={
        'registros_creados' : registros_creados,
        'usuarios_registrados' : usuarios_registrados,
        'numero_quejas' : numero_quejas,

    }
    
    return render(request, 'Admin/index.html', context)


@login_required(login_url='/Presentacion')
def sala_registros(request):

    registros_listos= DatosUsuario.objects.filter()

    context ={
        'registros_listos' : registros_listos
    }
    
    return render(request, 'OtrasRutas/registros.html', context)

@login_required(login_url='/Presentacion')
def sala_quejas(request):

    quejas_sugerencias = QuejaSugerencias.objects.filter()

    context ={
        'quejas_sugerencias' : quejas_sugerencias,
    }
    
    return render(request,'OtrasRutas/quejas.html',context)


def cerrar_sesion(request):
    logout(request)
    context ={
            
    }
    return render(request, 'Presentacion/index.html', context)