# Generated by Django 5.1.2 on 2024-11-08 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('Id_Municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Municipio.municipio')),
            ],
        ),
    ]