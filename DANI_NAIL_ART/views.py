from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Servicio
from django.contrib.auth.decorators import login_required
from .forms import Agendar_Servicio

def incio(request):
    titulo = "hello bich"
    return render(request, 'Login/inicio.html', {
        'titulo':titulo
    })

def servicios(request):
    return render(request, 'Servcios/Servicios.html')

def regitro(request):
    if request.method == 'GET':
        return render(request, 'Register/registrar.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('InicioSeccion')
            except IntegrityError:
                return render(request, 'Register/registrar.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'Register/registrar.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'Login/inicio.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Login/inicio.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('Servicios')
    
@login_required
def signout(request):
    logout(request)
    return redirect('inincio')


def añadir_Servicios( request ):
    if request.method == 'POST':
        form = Agendar_Servicio(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion =form.cleaned_data['descripcion']
            disponibilidad = form.cleaned_data['disponibilidad']
            precio = form.cleaned_data['precio']
            imagen = form.cleaned_data['imagen']
            Servicio.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                disponibilidad=disponibilidad,
                precio=precio,
                imagen=imagen,
            )
            return redirect('/servicios')
    else:
        form = Agendar_Servicio()

    return render(request, 'Servcios/Agregar_Servcios.html', {
        'form': form, 
    })
# Create your views here.

