from django.forms import ModelForm
from .models import CadastroCrianca


class CriancaForm(ModelForm):
    class Meta:
        model = CadastroCrianca
        fields = ['name', 'address', 'phone', 'data_nascimento', 'mae', 'pai']