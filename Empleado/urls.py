from django.urls import path
from . import views

urlpatterns = [
    path('registrar_empleado/', views.registrar_empleado, name='registrar_empleado'),
    path('historial_empleado/', views.historial_empleado, name='historial_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar_empleado/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
]
