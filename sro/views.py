from django.shortcuts import render

# Create your views here.
def receive_application(request):
	print(request.POST)
