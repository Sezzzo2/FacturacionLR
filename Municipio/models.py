from django.db import models

from django.db import models
from Clasificacion.models import Departamento  

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, null=False)  # Campo Nombre, NOT NULL
    Id_Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)  # Llave foránea a Departamento
    estado = models.BooleanField(default=True)  # Campo de estado


    def __str__(self):
        return self.nombre
    