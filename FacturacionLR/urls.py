"""
URL configuration for FacturacionLR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainApp.views import login_view, inicio_view
from mainApp.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='empleado_login'),  
    path('', inicio_view, name='inicio'), 
    path('municipio/', include('Municipio.urls')),  
    path('clasificacion/', include('Clasificacion.urls')),
    path('sede/', include('Sede.urls')),
    path('empleado/', include('Empleado.urls')),
    path('logout/', logout_view, name='logout'),
    path('aviso/', include('Aviso.urls')),
    path('factura/', include('Factura.urls')),
    path('cliente/', include('Cliente.urls'))
]
