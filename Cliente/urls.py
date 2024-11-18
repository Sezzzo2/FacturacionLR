from django.urls import path
from . import views

urlpatterns = [
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('historial_cliente/', views.historial_cliente, name='historial_cliente'),
    path('actualizar_cliente/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
]
