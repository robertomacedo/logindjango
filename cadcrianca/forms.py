from django.forms import ModelForm
from .models import CadastroCrianca
from django import forms


class CadastroCriancaForm(forms.ModelForm):
    class Meta:
        model = CadastroCrianca
        fields = ['name', 'address', 'phone', 'data_nascimento', 'mae', 'pai']
