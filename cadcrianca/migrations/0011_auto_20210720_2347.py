# Generated by Django 3.1.7 on 2021-07-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadcrianca', '0010_auto_20210718_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocrianca',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='criancas'),
        ),
    ]