from django.db import models

# Create your models here.
from apps.producto.models import Producto

class Ingreso(models.Model):
	id_ingreso = models.IntegerField(primary_key=True)
	fecha_ingreso = models.DateField()
	cantidad = models.IntegerField()
	producto = models.ManyToManyField(Producto)

	def __str__(self):
		return '{}'.format(self.id_ingreso)