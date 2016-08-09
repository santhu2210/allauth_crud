from django.shortcuts import render
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from allauthapp.forms import EmpForm
from allauthapp.models import Employee


# Create your views here.


def profile(request):
	print request
	if request.method == 'GET':
		return HttpResponse("sucessful login")
	else:
		return HttpResponse("failure to get values")
	return HttpResponse("unable to load data")


def insert(request):
	if request.method == 'GET':
		form = EmpForm()

	else:
		form = EmpForm(request.POST)
		if form.is_valid():
			emp_name = form.cleaned_data['emp_name']
			emp_id = form.cleaned_data['emp_id']
			email_id = form.cleaned_data['email_id']
			gen = form.cleaned_data['gen']
			dept = form.cleaned_data['dept']
			exp = form.cleaned_data['exp']
			skills = form.cleaned_data['skills']
			fdbk = form.cleaned_data['fdbk']
			E = Employee.objects.create(emp_name = emp_name,emp_id = emp_id, email_id = email_id, gen = gen, dept = dept, exp = exp, skills = skills, fdbk = fdbk)
			print emp_name,emp_id, email_id
			return HttpResponseRedirect('/show/')

	return render(request, 'insert.html',{'form': form})

def show(request):
	query_results = Employee.objects.all()
	return render(request, 'show.html',{'query_results': query_results})