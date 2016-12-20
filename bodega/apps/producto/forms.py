from django import forms

from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):
	
	class Meta:
		model = Producto

		fields = [
			'id_producto',
			'nombre',
			'descripcion',
			'categoria',
		]

		labels = {
			'id_producto': 'Id del producto',
			'nombre': 'Nombre del producto',
			'descripcion': 'Descripción del producto',
			'categoria': 'Categoria del producto',
		}


		widgets = {
			'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'categoria': forms.Select(attrs={'class': 'form-control'}),
		}
		






		
