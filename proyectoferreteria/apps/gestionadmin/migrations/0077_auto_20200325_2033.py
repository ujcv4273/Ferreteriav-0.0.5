# Generated by Django 3.0.4 on 2020-03-26 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0076_auto_20200325_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turnoempleado',
            old_name='horaEntrada',
            new_name='Hora_de_Entrada',
        ),
        migrations.RenameField(
            model_name='turnoempleado',
            old_name='horaSalida',
            new_name='Hora_de_Salida',
        ),
        migrations.RenameField(
            model_name='turnoempleado',
            old_name='idTurno',
            new_name='Id_Turno',
        ),
    ]
