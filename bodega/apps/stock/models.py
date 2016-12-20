from django.db import models

# Create your models here.
from apps.producto.models import Producto

class Stock(models.Model):
	id_stock = models.IntegerField(primary_key=True)
	cantidad = models.IntegerField()
	producto = models.ManyToManyField(Producto)

	def __str__(self):
		return '{} {}'.format(self.cantidad, self.producto)