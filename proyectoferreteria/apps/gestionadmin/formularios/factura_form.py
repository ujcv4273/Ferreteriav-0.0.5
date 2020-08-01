from django import forms
from proyectoferreteria.apps.gestionadmin.models import Factura
import datetime

class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura
    
        fields = [
            'Id_Factura',
            'Id_Empleado',
            'Id_Cliente',
            'Id_MetodoPago',
            'Id_FormaPago',
            'Numero_Sar',
            'Id_producto',
            'Codigo_CAI',
            'ISV18',
            'ISV15',
            'Total_Factura'
        ]

        labels = {
            'Id_Factura':'Id Factura',
            'Id_Empleado':'Empleado',
            'Id_Cliente':'Cliente',
            'Id_MetodoPago':'Método pago',
            'Id_FormaPago':'Forma pago',
            'Numero_Sar':'SAR',
            'Id_producto':'Producto',
            'Fecha':'Fecha',
            'Codigo_CAI':'CAI',
            'ISV18':'ISV 18%',
            'ISV15':'ISV 15%',
            'Total_Factura':'Total factura'
        }
        
        widgets = {
            'Id_Factura' :forms.TextInput(attrs={'class':'form-control'}),
            'Id_Empleado':forms.Select(attrs={'class':'form-control'}),
            'Id_Cliente':forms.Select(attrs={'class':'form-control'}),
            'Id_MetodoPago':forms.Select(attrs={'class':'form-control'}),
            'Id_FormaPago':forms.Select(attrs={'class':'form-control'}),
            'Numero_Sar':forms.TextInput(attrs={'class':'form-control'}),
            'Id_producto':forms.CheckboxSelectMultiple(),
            'Fecha':forms.DateTimeInput(),
            'Codigo_CAI':forms.TextInput(attrs={'class':'form-control'}),
            'ISV18':forms.TextInput(attrs={'class':'form-control'}),
            'ISV15':forms.TextInput(attrs={'class':'form-control'}),
            'Total_Factura':forms.TextInput(attrs={'class':'form-control'}),
        }