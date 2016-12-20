from django import forms

from apps.stock.models import Stock

class StockForm(forms.ModelForm):
	
	class Meta:
		model = Stock

		fields = [
			'id_stock',
			'cantidad',
			'producto',
			
		]

		labels = {
			'id_stock': 'Id del stock',
			'cantidad': 'Cantidad',
			'producto': 'Producto',
		}


		widgets = {
			'id_stock': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
			'producto': forms.CheckboxSelectMultiple(),
		}
		






		
