from django.db import models

# Create your models here.


class Categoria(models.Model):
	id_categoria = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=40)

	def __str__(self):
		return '{}'.format(self.nombre)