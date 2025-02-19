from django.db import models

# Create your models here.
class Caja(models.Model):
    #monto_disponible = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    monto_disponible = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Caja - ${self.monto_disponible}"

class MovimientoCaja(models.Model):
    TIPO_MOVIMIENTO = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
    ]

    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)

    def __str__(self):
        return f"{self.tipo_movimiento.capitalize()} de ${self.monto} por {self.nombre} el {self.fecha}"
    
#--------------------CREAR SIGNAL PARA CREAR LA CAJA AUTOMATICAMANTE----------------------------------
"""
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def crear_caja_inicial(sender, **kwargs):
    if sender.name == 'caja':  # Reemplaza 'caja' con el nombre de tu aplicación
        if not Caja.objects.exists():
            Caja.objects.create(monto_disponible=0.00)
"""