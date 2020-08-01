from django import forms
from proyectoferreteria.apps.gestionadmin.models import Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
    
        fields = [
            'Id_Proveedor',
            'Nombre_Proveedor',
            'Correo_Proveedor',
            'Direccion_Proveedor',
            'Telefono_Proveedor'
        ]

        labels = {
            'Id_Proveedor':'Id del proveedor',
            'Nombre_Proveedor':'Nombre del proveedor',
            'Correo_Proveedor':'Correo del proveedor',
            'Direccion_Proveedor':'Dirección del proveedor',
            'Telefono_Proveedor':'Telefono del proveedor'
        }
        
        widgets = {
            'Id_Proveedor' :forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_Proveedor':forms.TextInput(attrs={'class':'form-control'}),
            'Correo_Proveedor':forms.TextInput(attrs={'class':'form-control'}),
            'Direccion_Proveedor':forms.TextInput(attrs={'class':'form-control'}),
            'Telefono_Proveedor':forms.TextInput(attrs={'class':'form-control'}),
        }