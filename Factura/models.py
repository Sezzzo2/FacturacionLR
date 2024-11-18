from django.db import models
from Clasificacion.models import MetodoPago
from Sede.models import Sede
from django.contrib.auth.models import User  # Usa el modelo User de Django
from Cliente.models import Cliente

class Factura(models.Model):
    fecha = models.DateField(null=False)
    valor = models.IntegerField()
    Id_MetodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    Id_Sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    Id_Empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    Id_Cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    estado = models.BooleanField(default=True)  
    def __str__(self):
        return f"Factura {self.id} - {self.fecha} - {self.valor}"
