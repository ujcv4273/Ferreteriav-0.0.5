# Generated by Django 2.2.6 on 2020-06-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0134_remove_comprasenc_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasenc',
            name='no_factura',
            field=models.CharField(default='011-022-34853', max_length=100),
        ),
    ]
