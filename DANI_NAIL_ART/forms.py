from django import forms
from .models import Servicio
from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['servicio', 'fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }


class Agendar_Servicio(forms.Form):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'disponibilidad', 'precio', 'imagen']