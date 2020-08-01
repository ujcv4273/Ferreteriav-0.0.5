from django import forms
from proyectoferreteria.apps.gestionadmin.models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
    
        fields = [
            'Id_Cliente',
            'Nombre_Cliente',
            'Correo_Cliente',
            'Direccion_Cliente',
            'Telefono_Cliente'
        ]

        labels = {
            'Id_Cliente ':'IdCliente ',
            'Nombre_Cliente':'Nombre Cliente',
            'Correo_Cliente' : 'Correo',
            'Direccion_Cliente': 'Direccion',
            'Telefono_Cliente': 'Telefono'

        }

        widgets = {
            'Id_Cliente':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_Cliente':forms.TextInput(attrs={'class':'form-control'}),
            'Correo_Cliente':forms.TextInput(attrs={'class':'form-control'}),
            'Direccion_Cliente':forms.TextInput(attrs={'class':'form-control'}),
            'Telefono_Cliente':forms.TextInput(attrs={'class':'form-control'}),
        }