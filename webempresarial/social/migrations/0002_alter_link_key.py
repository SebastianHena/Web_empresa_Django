# Generated by Django 5.0 on 2024-01-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='key',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Nombre clave'),
        ),
    ]
