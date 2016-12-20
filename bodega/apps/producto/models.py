from django.db import models

# Create your models here.
from apps.categoria.models import Categoria


class Producto(models.Model):
	id_producto = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=40)
	categoria = models.ForeignKey (Categoria, null=True, blank=True, on_delete=models.CASCADE)
	

	def __str__(self):
		return '{}'.format(self.nombre)