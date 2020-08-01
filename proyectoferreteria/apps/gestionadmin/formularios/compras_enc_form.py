from django import forms
from proyectoferreteria.apps.gestionadmin.models import  ComprasEnc
class ComprasEncForm(forms.ModelForm):
    fecha_factura = forms.DateInput()
    
    class Meta:
        model=ComprasEnc
        fields=['cliente',
            'no_factura','fecha_factura','sub_total',
            'descuento','total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True