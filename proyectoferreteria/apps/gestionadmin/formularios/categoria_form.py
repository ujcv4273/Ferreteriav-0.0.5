from django import forms
from proyectoferreteria.apps.gestionadmin.models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
    
        fields = [
            'Id_Categoria',
            'Descripcion_Categoria'
        ]

        labels = {
            'Id_Categoria':'Id de la categoría',
            'Descripcion_Categoria':'Descripción de la categoría'
        }

        widgets = {
            'Id_Categoria':forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion_Categoria':forms.TextInput(attrs={'class':'form-control'}),
        }