from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from .models import Pago
from .forms import PagoForm
from prestamos.models import Prestamo
from caja.models import Caja
from interesT.models import InteresT

# Create your views here.
@never_cache
def payments(request):
    pagos = Pago.objects.all()
    return render(request, 'payments.html', {'pagos':pagos})

def register_pay(request, id=None):
    prestamo = None
    cliente = ""  # Inicializamos la variable cliente en blanco

    if id is not None:
        prestamo = get_object_or_404(Prestamo, id=id)
        cliente = prestamo.cliente  # Suponiendo que el modelo Prestamo tiene un campo cliente

    # from django.db import transaction
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # with transaction.atomic():  # Inicia una transacción
            # Guardar el pago en la base de datos
            pago = form.save()

           # Si el pago viene desde un préstamo, asignarlo automáticamente
            if prestamo:
                pago.prestamo = prestamo

            pago.save()  # Guardar pago en la BD

            # Actualizar caja
            caja = Caja.objects.first()
            if caja:
                caja.monto_disponible += pago.monto_pago
                caja.save()

            # Actualizar préstamo
            if pago.prestamo:
                pago.prestamo.monto -= pago.monto_pago
                pago.prestamo.interes -= pago.pagar_interes
                pago.prestamo.save()

            # Actualizar interes pagado
            interes = InteresT.objects.first()
            if interes:
                interes.interes_pagado += pago.pagar_interes
                print("------------------------interes_p")
                print(interes)
                interes.save()

            return redirect('payments')  # Redirige a una página de éxito
    else:
        # Si el préstamo ya está definido, inicializa el formulario con él
        form = PagoForm(initial={'prestamo': prestamo} if prestamo else {})
        #form = PagoForm()  # Crea un formulario vacío para GET

    return render(request, 'register_pay.html', {'form': form, 'prestamo': prestamo, 'cliente': cliente})