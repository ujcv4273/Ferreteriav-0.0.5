from django import forms
from proyectoferreteria.apps.gestionadmin.models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
    
        fields = [
            'Id_Producto',
            'Nombre_Producto',
            'Precio_Venta',
            'Precio_Compra',
            'Id_Marca',
            'Id_Categoria',
            'Id_Garantia',
            'Existencia',
            'Existencia_Minima'
        ]

        labels = {
            'Id_Producto':'Id del producto',
            'Nombre_Producto':'Nombre del producto',
            'Precio_Venta':'Precio de venta',
            'Precio_Compra':'Precio de compra',
            'Id_Marca':'Marca',
            'Id_Categoria':'Categoria',
            'Id_Garantia':'Garantia',
            'Existencia':'Existencia actual',
            'Existencia_Minima':'Existencia minima'
        }
        
        widgets = {
            'Id_Producto' :forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_Producto':forms.TextInput(attrs={'class':'form-control'}),
            'Precio_Venta':forms.TextInput(attrs={'class':'form-control'}),
            'Precio_Compra':forms.TextInput(attrs={'class':'form-control'}),
            'Id_Marca':forms.Select(attrs={'class':'form-control'}),
            'Id_Categoria':forms.Select(attrs={'class':'form-control'}),
            'Id_Garantia':forms.Select(attrs={'class':'form-control'}),
            'Existencia':forms.TextInput(attrs={'class':'form-control'}),
            'Existencia_Minima':forms.TextInput(attrs={'class':'form-control'}),
        }