# Generated by Django 3.1.1 on 2020-09-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_auto_20200920_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='graduacion_ojo_derecho',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='datosusuario',
            name='graduacion_ojo_izquierdo',
            field=models.CharField(max_length=10),
        ),
    ]
