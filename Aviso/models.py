from django.db import models
from Clasificacion.models import Categoria

class Aviso(models.Model):
    descripcion = models.CharField(max_length=255)
    Id_Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.descripcion[:50]} - {self.Id_Categoria.tipo}"

    class Meta:
        unique_together = ('descripcion', 'Id_Categoria') 