from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura
from Clasificacion.models import MetodoPago
from Sede.models import Sede
from Cliente.models import Cliente 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timezone   
from django.db.models import Sum, Count
from django.contrib import messages
import datetime  
from django.utils import timezone  

@login_required
def registrar_factura(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        valor = request.POST.get('valor')
        metodo_pago_id = request.POST.get('Id_MetodoPago')
        sede_id = request.POST.get('Id_Sede')
        cliente_id = request.POST.get('Id_Cliente')

        try:
            if fecha and datetime.datetime.strptime(fecha, "%Y-%m-%d").date() < timezone.now().date():
                messages.error(request, 'La fecha no puede ser anterior a la fecha actual.')
                return redirect('registrar_factura')
        except ValueError:
            messages.error(request, 'Formato de fecha no válido.')
            return redirect('registrar_factura')

        metodo_pago = get_object_or_404(MetodoPago, id=metodo_pago_id)
        sede = get_object_or_404(Sede, id=sede_id)
        cliente = get_object_or_404(Cliente, id=cliente_id)
        empleado = request.user

        factura = Factura(
            fecha=fecha,
            valor=valor,
            Id_MetodoPago=metodo_pago,
            Id_Sede=sede,
            Id_Empleado=empleado,
            Id_Cliente=cliente
        )
        factura.save()
        messages.success(request, 'Factura registrada exitosamente.')
        return redirect('registrar_factura')

    metodos_pago = MetodoPago.objects.filter(estado=True)
    sedes = Sede.objects.filter(estado=True)
    clientes = Cliente.objects.filter(estado=True)
    return render(request, 'registrar_factura.html', {
        'metodos_pago': metodos_pago,
        'sedes': sedes,
        'clientes': clientes
    })

def actualizar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        factura.fecha = request.POST.get('fecha')
        factura.valor = request.POST.get('valor')
        factura.Id_MetodoPago_id = request.POST.get('Id_MetodoPago')
        factura.Id_Sede_id = request.POST.get('Id_Sede')
        factura.Id_Cliente_id = request.POST.get('Id_Cliente')
        factura.save()
        messages.success(request, 'Factura actualizada correctamente.')
        return redirect('historial_factura')

def eliminar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        factura.estado = False  
        factura.save()         
        messages.success(request, 'Factura eliminada correctamente.')
        return redirect('historial_factura')

def historial_factura(request):
    facturas = Factura.objects.filter(estado=True).select_related(
        'Id_MetodoPago', 'Id_Sede', 'Id_Empleado', 'Id_Cliente__Id_Aviso__Id_Categoria'
    )
    metodos_pago = MetodoPago.objects.filter(estado=True)
    sedes = Sede.objects.filter(estado=True)
    clientes = Cliente.objects.filter(estado=True)
    return render(request, 'historial_factura.html', {
        'facturas': facturas,
        'metodos_pago': metodos_pago,
        'sedes': sedes,
        'clientes': clientes
    })

def resumen_facturas(request):
    facturas_activas = Factura.objects.filter(estado=True)

    total_facturas = facturas_activas.count()
    total_valor = facturas_activas.aggregate(Sum('valor'))['valor__sum'] or 0

    sede_con_mayor_venta = (
        facturas_activas.values('Id_Sede__nombre')
        .annotate(total_venta=Sum('valor'))
        .order_by('-total_venta')
        .first()
    )

    metodo_pago_mas_usado = (
        facturas_activas.values('Id_MetodoPago__nombre')
        .annotate(Count('id'))
        .order_by('-id__count')
        .first()
    )

    cantidad_facturas_por_sede = (
        facturas_activas.values('Id_Sede__nombre')
        .annotate(Count('id'))
        .order_by('-id__count')
    )

    contexto = {
        'total_facturas': total_facturas,
        'total_valor': total_valor,
        'sede_con_mayor_venta': sede_con_mayor_venta,
        'metodo_pago_mas_usado': metodo_pago_mas_usado,
        'cantidad_facturas_por_sede': cantidad_facturas_por_sede,
    }

    return render(request, 'resumen_facturas.html', contexto)
