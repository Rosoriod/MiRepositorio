from django import forms

from apps.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):
	
	class Meta:
		model = Categoria

		fields = [
			'id_categoria',
			'nombre',
			'descripcion',
		]

		labels = {
			'id_categoria': 'Id de la categoria',
			'nombre': 'Nombre de la categoria',
			'descripcion': 'Descripción de la categoria',
		}


		widgets = {
			'id_categoria': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
		}
		






		
