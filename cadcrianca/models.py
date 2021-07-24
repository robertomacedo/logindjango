from django.db import models
from django.contrib.auth.models import User


def upload_image_crianca(instance, filename):
    return f"{instance.pk} {filename}"


class CadastroCrianca(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, verbose_name='Nome')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contato')
    address = models.CharField(max_length=100, verbose_name='Endereço')
    data_nascimento = models.CharField(max_length=50, verbose_name='Data Nascimento')
    mae = models.CharField(max_length=100, verbose_name='Mãe')
    pai = models.CharField(max_length=100, null=True, blank=True, verbose_name='Pai')
    image = models.ImageField(upload_to="criancas", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    GENDER = (
        ('0', ''),
        ('man', 'homem'),
        ('woman', 'mulher'),
    )
    gender = models.CharField(
        'gênero',
        max_length=5,
        choices=GENDER,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'criança'
        verbose_name_plural = 'crianças'

    def __str__(self) -> str:
        return self.name


class Perfil(models.Model):
    name_completo = models.CharField(max_length=50, null=True, verbose_name='Nome')
    cpf = models.CharField(max_length=14, null=True, verbose_name='Cpf')
    telefone = models.CharField(max_length=16, null=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, null=True, verbose_name='Email')
    img = models.ImageField(upload_to='user', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_completo
