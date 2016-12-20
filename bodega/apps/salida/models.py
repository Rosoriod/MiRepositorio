from django.db import models

# Create your models here.
from apps.producto.models import Producto

class Salida(models.Model):
	id_salida = models.IntegerField(primary_key=True)
	fecha_salida = models.DateField()
	cantidad = models.IntegerField()
	producto = models.ManyToManyField(Producto)

	def __str__(self):
		return '{}'.format(self.id_salida)