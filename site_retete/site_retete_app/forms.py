from django import forms
from .models import Reteta

class AdaugaRetetaForm(forms.ModelForm):
    class Meta:
        model = Reteta
        fields = ['nume', 'timp', 'dificultate', 'ingrediente']

class ImportaRetetaForm(forms.Form):
    link_reteta = forms.URLField(label='Link reteta', max_length=200)