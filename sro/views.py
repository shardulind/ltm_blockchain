from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ApplicationQueue


# Create your views here.
@csrf_exempt
def receive_application(request):
	print(request.POST)
	print("anything")

	if request.method == "POST":
		print(request.POST)
		appn_in_window = ApplicationQueue(
						applicants_firstname = request.POST['fname'],
						applicants_middlename = request.POST['mname'],
						applicants_lastname = request.POST['lname'],
						applicants_mobno	= request.POST['mobno'],
						applicants_adharno	= request.POST['adno'],
						survey_no			= request.POST['propertyno'],
						)
		appn_in_window.save()


	return HttpResponse(request.POST)
