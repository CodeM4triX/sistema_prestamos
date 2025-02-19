from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from prestamos.models import Prestamo
from caja.models import Caja

# Create your models here.
class Pago(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)
    pagar_interes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Campo para el interés calculado
    fecha_pago = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} - {self.prestamo.cliente.nombre}"

