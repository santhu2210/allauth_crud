from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
	emp_name = models.CharField(max_length = 25)
	emp_id = models.CharField(max_length = 5)
	email_id = models.CharField(max_length = 30)
	gen = models.CharField(max_length=1)
	dept = models.CharField(max_length = 15)
	exp = models.CharField(max_length= 16)
	skills = models.CharField(max_length= 50)
	fdbk = models.CharField(max_length = 500)
	