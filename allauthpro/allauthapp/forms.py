
from django import forms


class EmpForm(forms.Form):
	emp_name = models.CharField(max_length = 25,required=True)
	emp_id = models.CharField(max_length = 5,unique=True,required=True )
	email_id = models.CharField(max_length = 30,unique=True,required=True)
	gender = (("MALE", "MALE"),("FEMALE", "FEMALE"))
	gen = models.CharField(max_length=1,choices=gender,default="MALE",required=True)
	department = (("OSA", "OSA"),("OSB", "OSB"),("MAINFRAME", "MAINFRAME"),("JAVA", "JAVA"),("GD", "GRAPHIC DESIGNER"))
	dept = models.CharField(max_length = 15,choices=dept,default="OSA",required=True)
	exp = models.CharField(max_length= 16,required=True)	
	skillset=(("JAVA","JAVA"),("PYTHON","PYTHON"),("RUBY","RUBY"))

	skills = models.CharField(max_length= 50,choices=skillset,default="PYTHON",required=True)
	fdbk = models.CharField(max_length = 500,required=True)
	