from django import forms
from proyectoferreteria.apps.gestionadmin.models import Marca

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
    
        fields = [
            'idMarca',
            'nombreMarca'
        ]

        labels = {
            'idMarca  ':'idMarca',
            'nombreMarca':'nombre de la marca'
        }

        widgets = {
            'idMarca':forms.TextInput(attrs={'class':'form-control'}),
            'nombreMarca':forms.TextInput(attrs={'class':'form-control'}),
        }