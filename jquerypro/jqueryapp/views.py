from django.shortcuts import render
from django.template import loader,Context, RequestContext

from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from jqueryapp.models import student


def insert(request):
	if request.method == 'POST':
		print(request.POST.get('nm1'))

		if request.is_ajax():

			NAME = request.POST.get('nm1')
			EMAILID = request.POST.get('em1')
			LOCATN = request.POST.get('lct1')

			can = student.objects.create(Name = NAME, Email = EMAILID, Locat = LOCATN)

			data = {"NAM": NAME, "EMAIL": EMAILID, "LOCATION": LOCATN}

			return JsonResponse(data)

		else:
			return HttpResponse("failed to get info")

	# else:
	# 	return HttpResponse("unable to post values")

	return render(request, 'insert.html')

def disp(request):
	query_results = student.objects.all()	
	return render(request, 'display.html', {'query_results': query_results})


def disp1(request):
	query_results = student.objects.all()	
	#data = {}
	usrlt = []
	# tempdata = {'hi':34}
	print query_results
	for i in query_results:
		print i.Name                             # printed in console
		print i.Email
		print i.Locat
		usrlt.append(i.Name)
		#tempusr = { "NAM":i.Name}
		
		#userData.update(tempusr)


	 	data = {"NAM": i.Name, "EMAIL": i.Email, "LOCATION": i.Locat}
	# 	userData.update(tempdata)

	print data

	return JsonResponse(data)


	#return HttpResponse("usrlt")
