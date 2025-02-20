from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from caja.models import Caja
from interesT.models import InteresT

# Create your views here.
@login_required
@never_cache
def home(request):
    total_caja = Caja.objects.get(id=1)  # Obtiene el registro con id=1
    interes, creado = InteresT.objects.get_or_create(defaults={'interes_total': 0.00})   # devuelve una tupla con dos valores get_or_create()
    suma_total = total_caja.monto_disponible + interes.interes_total

    return render(request, 'home/home.html', {'total_caja':total_caja, 'interes':interes, 'suma_total':suma_total})
