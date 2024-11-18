from django.db import models
from Aviso.models import Aviso  

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.IntegerField()
    correo_electronico = models.EmailField()
    Id_Aviso = models.ForeignKey(Aviso, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return self.nombre

    def __str__(self):
        return f"{self.nombre} - {self.identificacion}"
