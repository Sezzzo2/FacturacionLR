from django.db import models
from Municipio.models import Municipio  

class Sede(models.Model):
    nombre = models.CharField(max_length=100, null=False)  # Campo Nombre, NOT NULL
    direccion = models.CharField(max_length=255, null=False)  # Campo Dirección, NOT NULL
    Id_Municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)  # Llave foránea a Municipio
    estado = models.BooleanField(default=True)  # Campo de estado

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"
