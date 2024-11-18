from django.shortcuts import render, redirect, get_object_or_404
from .models import MetodoPago, Categoria, Departamento
from django.contrib import messages

def registrar_metodo_pago(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        if MetodoPago.objects.filter(nombre=nombre).exists():
            messages.error(request, 'Este método de pago ya existe.')
            return redirect('registrar_metodo_pago')

        MetodoPago.objects.create(nombre=nombre)
        messages.success(request, 'Método de pago registrado exitosamente.')
        return redirect('registrar_metodo_pago')
    
    return render(request, 'registrar_metodo_pago.html')

def historial_metodo_pago(request):
    metodos_pago = MetodoPago.objects.filter(estado=True)  
    return render(request, 'historial_metodopago.html', {'metodos_pago': metodos_pago})

def actualizar_metodo_pago(request, metodo_id):
    metodo = get_object_or_404(MetodoPago, id=metodo_id)
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        metodo.nombre = nuevo_nombre
        metodo.save()
        messages.success(request, 'Método de Pago actualizado correctamente.')
        return redirect('historial_metodo_pago')

def eliminar_metodo_pago(request, metodo_pago_id):
    metodo_pago = get_object_or_404(MetodoPago, id=metodo_pago_id)
    metodo_pago.estado = False  
    metodo_pago.save()
    messages.success(request, 'El método de pago ha sido eliminado exitosamente.')
    return redirect('historial_metodo_pago')


def registrar_categoria(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        if Categoria.objects.filter(tipo=tipo).exists():
            messages.error(request, 'Esta categoría ya existe.')
            return redirect('registrar_categoria')

        Categoria.objects.create(tipo=tipo)
        messages.success(request, 'Categoría registrada exitosamente.')
        return redirect('registrar_categoria')
    
    return render(request, 'registrar_categoria.html')

def historial_categoria(request):
    categorias = Categoria.objects.filter(estado=True) 
    return render(request, 'historial_categoria.html', {'categorias': categorias})

def actualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        nuevo_tipo = request.POST.get('tipo')
        categoria.tipo = nuevo_tipo
        categoria.save()
        messages.success(request, 'Categoría actualizada correctamente.')
        return redirect('historial_categoria')

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.estado=False
    categoria.save()
    messages.success(request, 'La categoría ha sido eliminada exitosamente.')
    return redirect('historial_categoria')

def registrar_departamento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip() 

        if Departamento.objects.filter(nombre__iexact=nombre).exists():  
            messages.error(request, 'El departamento ya está registrado.')
            return redirect('registrar_departamento')
        
        nuevo_departamento = Departamento(nombre=nombre)
        nuevo_departamento.save()
        messages.success(request, 'Departamento registrado exitosamente.')
        return redirect('registrar_departamento')

    return render(request, 'registrar_departamento.html')

def historial_departamento(request):
    departamentos = Departamento.objects.filter(estado=True)  
    return render(request, 'historial_departamento.html', {'departamentos': departamentos})

def actualizar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        departamento.nombre = nuevo_nombre
        departamento.save()
        messages.success(request, 'Departamento actualizado correctamente.')
        return redirect('historial_departamento')

def eliminar_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento, id=departamento_id)
    departamento.estado = False 
    departamento.save()
    messages.success(request, 'El departamento ha sido eliminado exitosamente.')
    return redirect('historial_departamento')