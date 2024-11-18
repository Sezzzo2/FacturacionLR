# Generated by Django 5.1.2 on 2024-11-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aviso', '0001_initial'),
        ('Clasificacion', '0002_alter_metodopago_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='aviso',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='descripcion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='aviso',
            unique_together={('descripcion', 'Id_Categoria')},
        ),
    ]
