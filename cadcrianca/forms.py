from django.forms import ModelForm
from .models import CadastroCrianca
from django import forms


class CriancaForm(ModelForm):
    class Meta:
        model = CadastroCrianca
        fields = ['name', 'address', 'phone', 'data_nascimento', 'mae', 'pai']