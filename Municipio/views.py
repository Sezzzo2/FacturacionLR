from django.shortcuts import render, redirect, get_object_or_404
from .models import Municipio
from Clasificacion.models import Departamento
from django.contrib import messages

def registrar_municipio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        departamento_id = request.POST.get('departamento')

        if Municipio.objects.filter(nombre=nombre, Id_Departamento_id=departamento_id).exists():
            messages.error(request, 'Este municipio ya existe en el departamento seleccionado.')
            return redirect('registrar_municipio')

        if nombre and departamento_id:
            departamento = Departamento.objects.get(id=departamento_id)
            Municipio.objects.create(nombre=nombre, Id_Departamento=departamento)
            messages.success(request, 'Municipio registrado exitosamente.')
            return redirect('registrar_municipio')
    
    departamentos = Departamento.objects.filter(estado = True)
    return render(request, 'registrar_municipio.html', {'departamentos': departamentos})

def historial_municipio(request):
    municipios = Municipio.objects.filter(estado=True) 
    departamentos = Departamento.objects.all()
    return render(request, 'historial_municipio.html', {'municipios': municipios, 'departamentos':departamentos})

def actualizar_municipio(request, municipio_id):
    municipio = get_object_or_404(Municipio, id=municipio_id)
    if request.method == 'POST':
        municipio.nombre = request.POST.get('nombre')
        departamento_id = request.POST.get('departamento')

        try:
            municipio.Id_Departamento = Departamento.objects.get(id=departamento_id)

            if Municipio.objects.filter(nombre=municipio.nombre, Id_Departamento_id=departamento_id).exclude(id=municipio_id).exists():
                messages.error(request, 'Un municipio con este nombre ya existe en el departamento seleccionado.')
            else:
                municipio.save()
                messages.success(request, 'Municipio actualizado correctamente.')
        except Departamento.DoesNotExist:
            messages.error(request, 'El departamento seleccionado no existe.')

        return redirect('historial_municipio')

    departamentos = Departamento.objects.filter(estado=True)
    return render(request, 'historial_municipio.html', {
        'municipios': Municipio.objects.all(),
        'departamentos': departamentos
    })

def eliminar_municipio(request, municipio_id):
    municipio = get_object_or_404(Municipio, id=municipio_id)
    municipio.estado = False 
    municipio.save()
    messages.success(request, 'El municipio ha sido eliminado exitosamente.')
    return redirect('historial_municipio')
