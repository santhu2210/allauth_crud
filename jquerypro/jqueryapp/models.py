from django.db import models
from django.contrib import admin

# Create your models here.

# class Candidate(models.Model):
# 	Name=models.CharField(max_length=200)
# 	Email=models.CharField(max_length=15)
# 	Locat=models.CharField(max_length =10)
# 	Pin = models.CharField(max_length =6)

class  student(models.Model):
	Name = models.CharField(max_length = 20)
	Email = models.CharField(max_length = 15)
	Locat = models.CharField(max_length = 25)


