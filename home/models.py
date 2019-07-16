from django.db import models

class Details(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField(max_length=256)
	phone = models.CharField(max_length=20,blank=True)
	description = models.TextField('What can we do for you?')

	def __str__(self):
		return self.email


	class Meta:
		verbose_name_plural = 'Details'

