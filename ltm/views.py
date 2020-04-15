from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from umbra.models import IPMapping

@csrf_exempt
def application_form(request):

	if request.method == 'POST':
		print(request.POST)
		var1 = IPMapping.objects.get(pincode = request.POST.get('pincode'))
		print(var1.ipaddress)
		return HttpResponse("Recieved data")

	else:
		return render(request, 'application_form.html')