from django import forms

from apps.salida.models import Salida

class SalidaForm(forms.ModelForm):
	
	class Meta:
		model = Salida

		fields = [
			'id_salida',
			'fecha_salida',
			'cantidad',
			'producto',
		]

		labels = {
			'id_salida': 'Id de la salida',
			'fecha_salida': 'Fecha de la salida',
			'cantidad': 'Cantidad',
			'producto': 'Producto saliente',
		}


		widgets = {
			'id_salida': forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_salida': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
			'producto': forms.CheckboxSelectMultiple(),
		}
		






		
