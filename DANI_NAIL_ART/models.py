from django.db import models
from django.core.validators import MinValueValidator


class Servicio(models.Model):
    nombre = models. CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    disponibilidad = models.BooleanField()
    precio = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0)])
    imagen = models.ImageField()

    def __str__(self) -> str:
        return self.nombre
# Create your models here.

class Cita(models.Model):
    servicio = models.CharField(max_length=50)
    # servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    hora = models.TimeField()