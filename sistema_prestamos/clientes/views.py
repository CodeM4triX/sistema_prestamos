from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

# Create your views here.
def clients(request):
    clientes = Cliente.objects.all()
    return render(request, 'clients.html', {'clients': clientes})

def register_clients(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')  # Redirige a una página de éxito o a la lista de clientes
    else:
        form = ClienteForm()
    
    return render(request, 'register_clients.html', {'form': form})
    #return render(request, 'register_clients.html') 