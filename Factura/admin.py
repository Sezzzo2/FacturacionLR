from django.contrib import admin
from .models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'valor', 'Id_MetodoPago', 'Id_Sede', 'Id_Empleado', 'Id_Cliente')
