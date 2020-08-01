# Generated by Django 2.2.6 on 2020-03-16 04:32

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0042_auto_20200315_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='correoProveedor',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccionProveedor',
            field=models.TextField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombreProveedor',
            field=models.CharField(max_length=35, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefonoProveedor',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero]),
        ),
    ]