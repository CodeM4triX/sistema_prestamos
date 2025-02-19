from django.shortcuts import render, redirect
from .models import  Caja, MovimientoCaja
from .forms import MovimientoCajaForm

# Create your views here.
def caja(request):
    #total_caja = Caja.objects.all()    # obtiene todos los registros de caja, en html se debe iterar sobre el queryset con bucle for
    #total_caja = Caja.objects.first()  # Obtiene el primer registro de Caja
    total_caja = Caja.objects.get(id=1)  # Obtiene el registro con id=1
    print(total_caja)
    movimiento = MovimientoCaja.objects.all()
    return render(request, 'caja.html', {'movimiento':movimiento, 'total_caja':total_caja})

def agregar_dinero_caja(request):
    if request.method == 'POST':
        form = MovimientoCajaForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            #caja = Caja.objects.first()  # Asumiendo que solo hay una caja

            # Obtener o crear la caja si no existe
            caja, created = Caja.objects.get_or_create(defaults={'monto_disponible': 0.00})

            if movimiento.tipo_movimiento == 'deposito':
                caja.monto_disponible = caja.monto_disponible + movimiento.monto
            elif movimiento.tipo_movimiento == 'retiro':
                if movimiento.monto > caja.monto_disponible:
                    form.add_error(None, "No hay suficiente dinero en la caja para realizar este retiro.")
                    return render(request, 'agregar_dinero_caja.html', {'form': form})
                caja.monto_disponible = caja.monto_disponible - movimiento.monto

            caja.save()
            movimiento.save()
            return redirect('caja')  # Redirigir a alguna vista después de guardar
    else:
        form = MovimientoCajaForm()

    return render(request, 'agregar_dinero_caja.html', {'form': form})