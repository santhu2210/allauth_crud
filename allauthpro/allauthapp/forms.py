
from django import forms


class EmpForm(forms.Form):
	emp_name = forms.CharField(max_length = 25)
	emp_id = forms.CharField(max_length = 5)
	email_id = forms.CharField(max_length = 30)
	gen = forms.CharField(max_length=1)
	dept = forms.CharField(max_length = 15)
	exp = forms.CharField(max_length= 16)
	skills = forms.CharField(max_length= 50)
	fdbk = forms.CharField(max_length = 500)