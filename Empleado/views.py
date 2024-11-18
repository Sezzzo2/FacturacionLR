from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado registrado exitosamente.')
            return redirect('registrar_empleado')
    else:
        form = EmpleadoForm()

    role_choices = Empleado.ROLE_CHOICES

    return render(request, 'registrar_empleado.html', {
        'form': form,
        'role_choices': role_choices
    })

def historial_empleado(request):
    empleados = Empleado.objects.filter(estado=True) 
    return render(request, 'historial_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        rol = request.POST.get('rol')

        empleado.user.username = username
        empleado.rol = rol

        empleado.user.save()
        empleado.save()

        messages.success(request, 'Empleado actualizado correctamente.')
        return redirect('historial_empleado')
    
    messages.error(request, 'Ocurrió un error al actualizar el empleado.')
    return redirect('historial_empleado')

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    empleado.estado = False  
    empleado.save()
    messages.success(request, 'Empleado eliminado exitosamente.')
    return redirect('historial_empleado')
