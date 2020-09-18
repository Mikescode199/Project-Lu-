from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import LoginForm, FormularioUser


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
        }
    
    return render(request, 'Presentacion/index.html', context)


#Sala de administración
def sala_administrador(request):
    context ={
    }
    
    return render(request, 'Admin/index.html', context)