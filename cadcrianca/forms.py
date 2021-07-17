from .models import CadastroCrianca, Perfil
from django import forms


class CadastroCriancaForm(forms.ModelForm):
    class Meta:
        model = CadastroCrianca
        fields = ['name', 'address', 'phone', 'data_nascimento', 'mae', 'pai']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['name_completo', 'cpf', 'telefone', 'email', 'usuario']


class EditarPerfilForm(forms.Form):
    def __init__(self, *args, **kwargs):
        perfil = Perfil.objects.get(id=kwargs.pop('id'))
        self.perfil = perfil
        super(EditarPerfilForm).__init__(*args, **kwargs)
        self.fields['name_completo'] = forms.CharField(max_length=50, initial=perfil.name_completo) 
        self.fields['cpf'] = cpf = models.CharField(max_length=14)
        self.fields['telefone'] = telefone = models.CharField(max_length=16)
        self.fields['email'] = email = models.EmailField(max_length=100)
