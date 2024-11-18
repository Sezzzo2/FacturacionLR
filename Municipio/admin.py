from django.contrib import admin
from .models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'Id_Departamento')
