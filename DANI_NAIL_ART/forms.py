from django import forms
from .models import Servicio

class Agendar_Servicio(forms.Form):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'disponibilidad', 'precio', 'imagen']