from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import CitaForm, Agendar_Servicio
from .models import Cita, Servicio
from django.urls import reverse
from django.contrib import messages


def incio(request):
    titulo = "hello bich"
    return render(request, 'Login/inicio.html', {
        'titulo':titulo
    })

def Menu(request):
    return render(request, 'Menu.html')

#--------------------REGISTRARSE-----------------------------

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

#----------------------INICIO DE SESIÓN----------------------------

def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'Login/inicio.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            
            return render(request, 'Login/inicio.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('Menu')
    
#----------------------CERRAR SESIÓN-----------------------------
    
@login_required
def signout(request):
    logout(request)
    return redirect('inincio')

#------------------------CREAR CITA-------------------------------

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            # Verificar si ya existe una cita con la misma fecha y hora
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']
            if Cita.objects.filter(fecha=fecha, hora=hora).exists():
                # Si la cita ya existe, establece citaExistente como True
                citaExistente = True
            else:
                # Si no existe, establece citaExistente como False
                citaExistente = False
                
            if citaExistente:
                # Si la cita ya existe, muestra un mensaje de error en JSON
                response_data = {'error': 'La fecha y hora ya están en uso.'}
                return JsonResponse(response_data, status=400)
            else:
                # Si no existe, guarda la nueva cita
                form.save()
                # Redirige al usuario a la lista de citas o la página que desees
                return HttpResponseRedirect(reverse('lista_citas'))
        else:
            # Manejar errores de validación del formulario
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = CitaForm()
    return render(request, 'Citas/crear_cita.html', {'form': form})

#-------------------LISTA DE CITAS------------------------------------------

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'Citas/lista_citas.html', {'citas': citas})

#---------------------------EDITAR CITA-------------------------------------

def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'Citas/editar_cita.html', {'form': form, 'cita': cita})

#----------------------ELIMINAR CITA----------------------------------

def eliminar_cita(request, cita_id):
    try:
        cita = Cita.objects.get(id=cita_id)
        cita.delete()
        messages.success(request, 'La cita ha sido eliminada exitosamente.')
    except Cita.DoesNotExist:
        messages.error(request, 'La cita no se encontró o no pudo ser eliminada.')

    return redirect(reverse('lista_citas'))

#---------------------------AÑADIR SERVICIO---------------------------------

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
            return redirect('/Servicios_agendados')
    else:
        form = Agendar_Servicio()

    return render(request, 'Servicios/Agregar_Servcios.html', {
        'form': form, 
    })



# Create your views here.

# def añadir_Servicios( request ):
#     if request.method == 'POST':
#         return render( request, 'Servicios/Servicios.html', {
#             'form':Agendar_Servicio()
#         })
#     else:
#         nombre = request.POST['nombre']
#         descripcion = request.POST['descripcion']
#         disponibilidad = request.POST['disponibilidad']
#         precio = request.POST['precio']
#         imagen = request.POST['imagen']
#         Servicio.objects.create(nombre=nombre, descripcion=descripcion, disponibilidad=disponibilidad, precio=precio, imagen=imagen)
#         return redirect('/Agregar_Servicio')
