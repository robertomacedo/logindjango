# Generated by Django 3.1.7 on 2021-06-24 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadcrianca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastrocrianca',
            options={'ordering': ('name',), 'verbose_name': 'criança', 'verbose_name_plural': 'crianças'},
        ),
    ]
