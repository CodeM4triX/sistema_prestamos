from django.db import models
from clientes.models import Cliente
from interesT.models import InteresT

# Create your models here.
class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, default=2)
    interes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Campo para el interés calculado
    fecha_inicio = models.DateField(auto_now_add=True)
    plazo = models.IntegerField()  # Plazo en meses

    def __str__(self):
        return f"Préstamo {self.id} - {self.cliente.nombre}"

