# Generated by Django 5.1.2 on 2024-11-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Municipio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]