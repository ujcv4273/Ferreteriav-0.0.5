from django import forms
from proyectoferreteria.apps.gestionadmin.models import FacturaDetalle

class FacturaDetalleForm(forms.ModelForm):

    class Meta:
        model = FacturaDetalle
    
        fields = [
            'Id_Factura_Detalle',
            'Id_Factura_Encabezado',
            'Id_Producto',
            'Cantidad'
        ]

        labels = {
            'Id_Factura_Detalle' : 'Id del detalle de factura',
            'Id_Factura_Encabezado' : 'Id del encabezado de factura',
            'Id_Producto' : 'Id de los productos',
            'Cantidad' : 'Cantidad de productos'
        }

        widgets = {
            'Id_Factura_Detalle':forms.TextInput(attrs={'class':'form-control'}),
            'Id_Factura_Encabezado':forms.Select(attrs={'class':'form-control'}),
            'Id_Producto':forms.Select(attrs={'class':'form-control'}),
            'Cantidad':forms.TextInput(attrs={'class':'form-control'}),
        }