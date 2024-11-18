from django.urls import path
from . import views

urlpatterns = [
    path('registrar_aviso/', views.registrar_aviso, name='registrar_aviso'),
    path('historial_aviso/', views.historial_aviso, name='historial_aviso'),
    path('actualizar/<int:aviso_id>/', views.actualizar_aviso, name='actualizar_aviso'),
    path('eliminar/<int:aviso_id>/', views.eliminar_aviso, name='eliminar_aviso'),
]
