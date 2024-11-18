from django.urls import path
from . import views

urlpatterns = [
    path('registrar_municipio/', views.registrar_municipio, name='registrar_municipio'),
    path('historial_municipio/', views.historial_municipio, name='historial_municipio'),
    path('actualizar_municipio/<int:municipio_id>/', views.actualizar_municipio, name='actualizar_municipio'),
    path('eliminar_municipio/<int:municipio_id>/', views.eliminar_municipio, name='eliminar_municipio'),
]
