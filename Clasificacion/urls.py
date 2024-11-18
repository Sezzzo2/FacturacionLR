from django.urls import path
from . import views

urlpatterns = [
    path('registrar_metodo_pago/', views.registrar_metodo_pago, name='registrar_metodo_pago'),
    path('historial_metodo_pago/', views.historial_metodo_pago, name='historial_metodo_pago'),
    path('actualizar_metodo_pago/<int:metodo_id>/', views.actualizar_metodo_pago, name='actualizar_metodo_pago'),
    path('eliminar_metodo_pago/<int:metodo_pago_id>/', views.eliminar_metodo_pago, name='eliminar_metodo_pago'),

    path('registrar_categoria/', views.registrar_categoria, name='registrar_categoria'),
    path('historial_categoria/', views.historial_categoria, name='historial_categoria'),
    path('actualizar_categoria/<int:categoria_id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('eliminar_categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),

    path('registrar_departamento/', views.registrar_departamento, name='registrar_departamento'),
    path('historial_departamento/', views.historial_departamento, name='historial_departamento'),
    path('actualizar_departamento/<int:departamento_id>/', views.actualizar_departamento, name='actualizar_departamento'),
    path('eliminar_departamento/<int:departamento_id>/', views.eliminar_departamento, name='eliminar_departamento'),
]
