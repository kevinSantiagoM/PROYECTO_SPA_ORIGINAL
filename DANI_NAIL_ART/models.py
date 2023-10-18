from django.db import models
from django.core.validators import MinValueValidator


class Cita(models.Model):
    servicio = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

class Servicio(models.Model):
    nombre = models. CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    disponibilidad = models.BooleanField()
    precio = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0)])
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
# Create your models here.
