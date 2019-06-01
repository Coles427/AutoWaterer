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
	
class WaterDat(models.Model):
	def __int__(self):
		return self.plant_num
	plant_num = models.IntegerField()
	current_level = models.IntegerField()
	current_time = models.DateTimeField(auto_now = False, auto_now_add = True)