from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib import messages
from interesT.models import InteresT
from caja.models import Caja
from .models import Prestamo
from .forms import PrestamoForm

# Create your views here.
@never_cache
def loans(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'loans.html', {'prestamos':prestamos})

def register_loan(request):
    caja = Caja.objects.first()  # Obtener la instancia de la caja (asumiendo que solo hay una)
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            # Obtener el value de los campos
            monto_solicitado = form.cleaned_data['monto']
            interesCampo = form.cleaned_data['interes']

            interes, created = InteresT.objects.get_or_create(defaults={'interes_total':0.00})
            if interes:
                interes.interes_total += interesCampo
                interes.save()

            #caja = Caja.objects.first()  # Obtener la instancia de la caja (asumiendo que solo hay una)
            if monto_solicitado <= caja.monto_disponible:
                # Registrar el préstamo
                prestamo = form.save()
                # Actualizar el monto disponible en la caja
                caja.monto_disponible = caja.monto_disponible - monto_solicitado
                caja.save()
                messages.success(request, 'Préstamo registrado correctamente.')
                return redirect('loans')  # Redirigir a la lista de préstamos
            else:
                messages.error(request, 'Fondos insuficientes en la caja.')
        else:
            messages.error(request, 'Error en el formulario. Revise los datos.')
    else:
        form = PrestamoForm()
    
    return render(request, 'register_loan.html', {'form': form, 'monto_disponible': caja.monto_disponible})