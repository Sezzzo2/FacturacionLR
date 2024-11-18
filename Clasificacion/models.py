from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    estado = models.BooleanField(default=True) 
    def __str__(self):
        return self.tipo

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    estado = models.BooleanField(default=True) 

    def __str__(self):
        return self.nombre
