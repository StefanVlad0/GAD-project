from django import forms
from .models import Reteta

class AdaugaRetetaForm(forms.ModelForm):
    class Meta:
        model = Reteta
        fields = ['nume', 'timp', 'dificultate', 'ingrediente']