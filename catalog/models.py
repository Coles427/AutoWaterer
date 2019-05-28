from django.db import models

# Create your models here.

test = (
 ('A', '1'),
 ('B', '2'),
 ('C', '3'),
 ('n', 'New Plant'),
)
class Plant(models.Model):
	def __str__(self):
		return self.plant_type
	
	plant_type = models.CharField(
	max_length = 25,
	)
	min_water = models.IntegerField()
	max_water = models.IntegerField()
	