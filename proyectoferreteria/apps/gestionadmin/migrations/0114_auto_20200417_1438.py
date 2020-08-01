# Generated by Django 3.0.4 on 2020-04-17 14:38

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0113_auto_20200417_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='ISV15',
            field=models.FloatField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos], verbose_name='ISV al 15%'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='ISV18',
            field=models.FloatField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos], verbose_name='ISV al 18%'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Total_Factura',
            field=models.FloatField(verbose_name='Total'),
        ),
    ]
