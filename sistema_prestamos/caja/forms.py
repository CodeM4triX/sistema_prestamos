from django import forms
from .models import MovimientoCaja

class MovimientoCajaForm(forms.ModelForm):
    class Meta:
        model = MovimientoCaja
        fields = ['nombre', 'monto', 'tipo_movimiento']