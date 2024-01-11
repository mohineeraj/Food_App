from django.db import models

# Create your models here.
class Account(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	Username=models.CharField(max_length=50)
	PASSWORD=models.CharField(max_length=50)
	Confirm_Password=models.CharField(max_length=50)
	EMAIL=models.EmailField(max_length=50)