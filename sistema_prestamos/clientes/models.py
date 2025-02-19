from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    #direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    #email = models.EmailField()

    def __str__(self):
        return self.nombre
