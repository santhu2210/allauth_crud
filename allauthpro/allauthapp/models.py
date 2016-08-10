from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
	emp_name = models.CharField(max_length = 25)
	emp_id = models.CharField(max_length = 5 unique=True)
	email_id = models.CharField(max_length = 30 unique=True)
	gender = (("MALE", "MALE"),("FEMALE", "FEMALE"))
	gen = models.CharField(max_length=1,choices=gender,default="MALE")
	department = (("OSA", "OSA"),("OSB", "OSB"),("MAINFRAME", "MAINFRAME"),("JAVA", "JAVA"),("GD", "GRAPHIC DESIGNER"))
	dept = models.CharField(max_length = 15,choices=dept,default="OSA")
	exp = models.CharField(max_length= 16)	
	skillset=(("JAVA","JAVA"),("PYTHON","PYTHON"),("RUBY","RUBY"))

	skills = models.CharField(max_length= 50,choices=skillset,default="PYTHON")
	fdbk = models.CharField(max_length = 500)
	