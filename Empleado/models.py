from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    ROLE_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Secretario', 'Secretario'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    rol = models.CharField(max_length=50, choices=ROLE_CHOICES)
    estado = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
