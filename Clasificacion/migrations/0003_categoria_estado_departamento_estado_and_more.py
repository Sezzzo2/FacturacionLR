# Generated by Django 5.1.2 on 2024-11-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clasificacion', '0002_alter_metodopago_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='departamento',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='metodopago',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
