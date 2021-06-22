from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(CadastroCrianca)
class CadastroCrianacaAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'mae', 'pai')
    search_fields = ('name',)