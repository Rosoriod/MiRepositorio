from django import forms

from apps.ingreso.models import Ingreso

class IngresoForm(forms.ModelForm):
	
	class Meta:
		model = Ingreso

		fields = [
			'id_ingreso',
			'fecha_ingreso',
			'cantidad',
			'producto',
		]

		labels = {
			'id_ingreso': 'Id del ingreso',
			'fecha_ingreso': 'Fecha del ingreso',
			'cantidad': 'Cantidad',
			'producto': 'Producto que ingresa',
		}


		widgets = {
			'id_ingreso': forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_ingreso': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
			'producto': forms.CheckboxSelectMultiple(),
		}
		





		
