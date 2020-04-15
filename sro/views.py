from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def receive_application(request):
	print(request.POST)
	print("anything")
	return HttpResponse(request.POST)
