from django.shortcuts import render, redirect, get_object_or_404
from .models import Sede
from Municipio.models import Municipio
from django.contrib import messages

def registrar_sede(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        municipio_id = request.POST.get('municipio')

        if Sede.objects.filter(nombre=nombre).exists():
            messages.error(request, 'Una sede con este nombre ya existe.')
            return redirect('registrar_sede')

        if nombre and direccion and municipio_id:
            municipio = Municipio.objects.get(id=municipio_id)
            Sede.objects.create(nombre=nombre, direccion=direccion, Id_Municipio=municipio)
            messages.success(request, 'Sede registrada exitosamente.')
            return redirect('registrar_sede')

    municipios = Municipio.objects.all()
    return render(request, 'registrar_sede.html', {'municipios': municipios})

def historial_sede(request):
    sedes = Sede.objects.filter(estado=True)
    municipios = Municipio.objects.all()
    return render(request, 'historial_sede.html', {'sedes': sedes, 'municipios': municipios})

def actualizar_sede(request, sede_id):
    sede = get_object_or_404(Sede, id=sede_id)
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        nueva_direccion = request.POST.get('direccion')
        municipio_id = request.POST.get('municipio')

        if Sede.objects.filter(nombre=nuevo_nombre).exclude(id=sede.id).exists():
            messages.error(request, 'Una sede con este nombre ya existe.')
            return redirect('historial_sede')

        sede.nombre = nuevo_nombre
        sede.direccion = nueva_direccion
        sede.Id_Municipio = Municipio.objects.get(id=municipio_id)
        sede.save()
        messages.success(request, 'Sede actualizada correctamente.')
        return redirect('historial_sede')

def eliminar_sede(request, sede_id):
    sede = get_object_or_404(Sede, id=sede_id)
    sede.estado = False 
    sede.save()
    messages.success(request, 'La sede ha sido eliminada exitosamente.')
    return redirect('historial_sede')
