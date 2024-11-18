from django.contrib import admin
from .models import Sede

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'Id_Municipio')
