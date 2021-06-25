from django.db import models


#CREACION DE TABLAS PARA LA BD
class lonches (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb


class gordas (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb

class tacos (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb


