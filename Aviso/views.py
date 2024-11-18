from django.shortcuts import render, redirect, get_object_or_404
from .models import Aviso
from Clasificacion.models import Categoria
from django.contrib import messages

def registrar_aviso(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('Id_Categoria')

        if not descripcion or not categoria_id:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'registrar_aviso.html')

        if Aviso.objects.filter(descripcion=descripcion, Id_Categoria_id=categoria_id).exists():
            messages.error(request, 'Este aviso ya existe con la misma categoría.')
            return render(request, 'registrar_aviso.html')

        categoria = Categoria.objects.get(id=categoria_id)
        aviso = Aviso(descripcion=descripcion, Id_Categoria=categoria)
        aviso.save()

        messages.success(request, 'Aviso registrado exitosamente.')

    categorias = Categoria.objects.all()
    return render(request, 'registrar_aviso.html', {'categorias': categorias})

def historial_aviso(request):
    avisos = Aviso.objects.filter(estado=True)  
    categorias = Categoria.objects.all()
    return render(request, 'historial_aviso.html', {
        'avisos': avisos,
        'categorias': categorias
    })

def actualizar_aviso(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id)
    if request.method == 'POST':
        aviso.descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        
        try:
            aviso.Id_Categoria = Categoria.objects.get(id=categoria_id)
            aviso.save()
            messages.success(request, 'Aviso actualizado exitosamente.')
        except Categoria.DoesNotExist:
            messages.error(request, 'La categoría seleccionada no existe.')
        
        return redirect('historial_aviso')

    categorias = Categoria.objects.all()
    return render(request, 'historial_aviso.html', {
        'avisos': Aviso.objects.all(),
        'categorias': categorias
    })

def eliminar_aviso(request, aviso_id):
    aviso = get_object_or_404(Aviso, id=aviso_id)
    aviso.estado = False  
    aviso.save()
    messages.success(request, 'El aviso se he eliminado.')
    return redirect('historial_aviso')