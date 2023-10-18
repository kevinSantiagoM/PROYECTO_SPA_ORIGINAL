from django.urls import path
from . import views

urlpatterns = [
    path('regitrar/', views.regitro, name='Registrar'),
    path('', views.inicio_sesion, name='InicioSeccion'),
    path('logout/', views.signout, name='Salir'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('citas_agendadas/', views.lista_citas, name='lista_citas'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
    path('Servicios', views.servicios, name='Servicios'),
    path('Agregar_servicio/', views.añadir_Servicios, name='Agregar_Servicio')
]
