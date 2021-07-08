from django.contrib import admin
from . models import CadastroCrianca, Perfil


# Register your models here.
@admin.register(CadastroCrianca)
class CadastroCrianacaAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'mae', 'address')
    search_fields = ('name',)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('name_completo', 'cpf', 'telefone', 'email', 'usuario')
    search_fields = ('name_completo',)
