from django.db import models

# Create your models here.


class Amigo(models.Model): 
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255, null=True,blank=True)
	domicilio = models.CharField(max_length=255)

	class Meta: 
		db_table = 'amigos'

	def __str__(self): 
		return self.nombre