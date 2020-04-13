from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def application_form(request):

	if request.method == 'POST':
		print(request.POST)
		return HttpResponse("Recieved data")

	else:
		return render(request, 'application_form.html')