from django.db import models

# Create your models here.

class CadastroCrianca(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contato')
    address = models.CharField(max_length=100, verbose_name='Endereço')
    data_nascimento = models.CharField(max_length=50, verbose_name='Data Nascimento')
    mae = models.CharField(max_length=100, verbose_name='Mãe')
    pai = models.CharField(max_length=100, null=True, blank=True, verbose_name='Pai')
    image = models.ImageField(upload_to='media', null=True, blank=True)
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
        verbose_name = 'child'
        verbose_name_plural = 'childs'

    def __str__(self):
        return self.name
