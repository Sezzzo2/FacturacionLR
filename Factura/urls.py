from django.urls import path
from . import views

urlpatterns = [
    path('registrar_factura/', views.registrar_factura, name='registrar_factura'),
    path('historial_factura/', views.historial_factura, name='historial_factura'),
    path('actualizar_factura/<int:factura_id>/', views.actualizar_factura, name='actualizar_factura'),
    path('eliminar_factura/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),
    path('resumen_facturas/', views.resumen_facturas, name='resumen_facturas'),  
]