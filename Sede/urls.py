from django.urls import path
from . import views

urlpatterns = [
    path('registrar_sede/', views.registrar_sede, name='registrar_sede'),
    path('historial/', views.historial_sede, name='historial_sede'),
    path('actualizar/<int:sede_id>/', views.actualizar_sede, name='actualizar_sede'),
    path('eliminar/<int:sede_id>/', views.eliminar_sede, name='eliminar_sede'),
]
