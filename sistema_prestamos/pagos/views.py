from django.shortcuts import render, redirect
from .models import Pago
from .forms import PagoForm
from caja.models import Caja

# Create your views here.
def payments(request):
    pagos = Pago.objects.all()
    return render(request, 'payments.html', {'pagos':pagos})

def register_pay(request):
    # from django.db import transaction
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # with transaction.atomic():  # Inicia una transacción
            # Guardar el pago en la base de datos
            pago = form.save()

            # Lógica para actualizar la caja y el préstamo
            caja = Caja.objects.first()
            if caja:
                # Sumar el monto del pago al monto disponible en la caja
                caja.monto_disponible += pago.monto_pago
                caja.save()
            
            # Restar el monto del pago del monto del préstamo
            prestamo = pago.prestamo

            print(pago)
            prestamo.monto -= pago.monto_pago
            prestamo.interes = prestamo.interes - pago.pagar_interes
            prestamo.save()
            # Restar el interes_pagado del interes del prestamo


            return redirect('payments')  # Redirige a una página de éxito
    else:
        form = PagoForm()  # Crea un formulario vacío para GET

    return render(request, 'register_pay.html', {'form': form})