# Generated by Django 3.1.1 on 2020-09-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_quejasugerencias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='graduacion_ojo_derecho',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='datosusuario',
            name='graduacion_ojo_izquierdo',
            field=models.CharField(max_length=500),
        ),
    ]
