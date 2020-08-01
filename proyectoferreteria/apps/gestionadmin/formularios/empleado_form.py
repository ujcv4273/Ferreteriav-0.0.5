from django import forms
from proyectoferreteria.apps.gestionadmin.models import  Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
    
        fields = [
            'Id_Empleado',
            'Id_Turno',
            'Id_Planilla',
            'Nombre_Empleado',
            'Direccion_Empleado',
            'Telefono_Empleado'
        ]

        labels = {
            'Id_Empleado':'Id_Empleado ',
            'Id_Turno':'Id_Turno',
            'Id_Planilla' : 'Id_Planilla',
            'Nombre_Empleado': 'Nombre Del Empleado',
            'Direccion_Empleado': 'Direccion',
            'Telefono_Empleado': 'Telefono',

        }

        widgets = {
            'Id_Empleado':forms.TextInput(attrs={'class':'form-control'}),
            'Id_Turno':forms.TextInput(attrs={'class':'form-control'}),
            'Id_Planilla':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_Empleado':forms.TextInput(attrs={'class':'form-control'}),
            'Direccion_Empleado':forms.TextInput(attrs={'class':'form-control'}),
            'Telefono_Empleado':forms.TextInput(attrs={'class':'form-control'}),
        }