from django import forms
from proyectoferreteria.apps.gestionadmin.models import Planilla

class PlanillaForm(forms.ModelForm):

    class Meta:
        model = Planilla
    
        fields = [
            'Id_Planilla',
            'Sueldo_Base',
            'IHSS',
            'RAP'
        ]

        labels = {
            'Id_Planilla ':'IdPlanilla',
            'Sueldo_Base':'Su sueldo',
            'IHSS' : 'Numero de seguro',
            'RAP': 'Numero de rap'
        }

        widgets = {
            'Id_Planilla':forms.TextInput(attrs={'class':'form-control'}),
            'Sueldo_Base':forms.TextInput(attrs={'class':'form-control'}),
            'IHSS':forms.TextInput(attrs={'class':'form-control'}),
            'RAP':forms.TextInput(attrs={'class':'form-control'}),
        }