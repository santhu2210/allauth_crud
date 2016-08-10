
from django import forms


class EmpForm(forms.Form):
	emp_name = forms.CharField()
	emp_id = forms.CharField()
	email_id = forms.CharField()
	gender = (("MALE", "MALE"),("FEMALE", "FEMALE"))
	gen = forms.ChoiceField(choices=gender)
	department = (("OSA", "OSA"),("OSB", "OSB"),("MAINFRAME", "MAINFRAME"),("JAVA", "JAVA"),("GD", "GRAPHIC DESIGNER"))
	dept = forms.ChoiceField(choices=department)
	exp = forms.CharField()	
	skillset=(("JAVA","JAVA"),("PYTHON","PYTHON"),("RUBY","RUBY"))

	skills = forms.ChoiceField(choices=skillset)
	fdbk = forms.CharField()