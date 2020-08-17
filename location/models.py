from django.db import models

class State(models.Model):
	name = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=10)
	state = models.ForeignKey('State', on_delete=models.CASCADE)

	class Meta:
		unique_together = [['state', 'name']]

	def __str__(self):
		return self.name

class ZipCode(models.Model):
	code = models.CharField(max_length=10)
	city = models.ForeignKey('City', on_delete=models.CASCADE)

	def __str__(self):
		return self.code
