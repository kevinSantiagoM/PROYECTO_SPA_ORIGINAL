from django.urls import path
from . import views

urlpatterns = [
    path('regitrar/', views.regitro, name='Registrar'),
    path('', views.inicio_sesion, name='InicioSeccion'),
    path('logout/', views.signout, name='Salir'),
    path('Servicios', views.servicios, name='Servicios'),
    path('Agregar_servicio/', views.añadir_Servicios, name='Agregar_Servicio')
]