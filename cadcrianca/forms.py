from .models import CadastroCrianca, Perfil
from django import forms


class CadastroCriancaForm(forms.ModelForm):
    class Meta:
        model = CadastroCrianca
        fields = ['name', 'address', 'phone', 'data_nascimento', 'mae', 'pai']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('name_completo', 'cpf', 'telefone', 'email', 'usuario')
