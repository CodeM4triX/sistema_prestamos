from django.db import models

# Create your models here.
class InteresT(models.Model):
    interes_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Interes - ${self.interes_total}"