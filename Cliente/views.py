from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from Aviso.models import Aviso
from django.contrib import messages

def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        identificacion = request.POST.get('identificacion')
        correo_electronico = request.POST.get('correo_electronico')
        aviso_id = request.POST.get('Id_Aviso')

        aviso = Aviso.objects.get(id=aviso_id)

        if Cliente.objects.filter(identificacion=identificacion).exists():
            messages.error(request, 'Un cliente con esta identificación ya existe.')
            return redirect('registrar_cliente')

        Cliente.objects.create(
            nombre=nombre,
            identificacion=identificacion,
            correo_electronico=correo_electronico,
            Id_Aviso=aviso
        )
        messages.success(request, 'Cliente registrado exitosamente.')
        return redirect('registrar_cliente')

    avisos = Aviso.objects.filter(estado=True)
    return render(request, 'registrar_cliente.html', {'avisos': avisos})

def historial_cliente(request):
    avisos = Aviso.objects.filter(estado=True) 
    clientes = Cliente.objects.filter(estado=True)  
    return render(request, 'historial_cliente.html', {'clientes': clientes,'avisos':avisos})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    avisos = Aviso.objects.filter(estado=True) 

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.identificacion = request.POST.get('identificacion')
        cliente.correo_electronico = request.POST.get('correo_electronico')
        aviso_id = request.POST.get('Id_Aviso')
        cliente.Id_Aviso = Aviso.objects.get(id=aviso_id)

        if Cliente.objects.filter(identificacion=cliente.identificacion).exclude(id=cliente_id).exists():
            messages.error(request, 'Un cliente con esta identificación ya existe.')
            return redirect('historial_cliente')

        cliente.save()
        messages.success(request, 'Cliente actualizado correctamente.')
        return redirect('historial_cliente')

    return render(request, 'historial_cliente.html', {'cliente': cliente, 'avisos': avisos})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.estado = False  
    cliente.save()
    messages.success(request, 'Cliente eliminado exitosamente.')
    return redirect('historial_cliente')
