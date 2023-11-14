from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio_sesion, name='InicioSeccion'),
    path('regitrar/', views.regitro, name='Registrar'),
    path('logout/', views.signout, name='Salir'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('citas_agendadas/', views.lista_citas, name='lista_citas'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
    path('Menu', views.Menu, name='Menu'),
    path('Agregar_servicio/', views.añadir_Servicios, name='Agregar_Servicio'),
    path('Servicios_agendados/', views.Servicios, name='Servicios_agendados')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)