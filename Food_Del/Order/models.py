from django.db import models

# Create your models here.
class FoodMenu(models.Model):
	Item=models.CharField(max_length=50)
	price=models.IntegerField()

	def __str__(self):
		return self.Item

class Ord_ADD(models.Model):
	Area=models.CharField(max_length=500)
	City=models.CharField(max_length=100)
	Pincode=models.CharField(max_length=6)
	Mnumber=models.IntegerField()
	def __str__(self):
		return self.Area
