from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from umbra.models import IPMapping
import requests	


@csrf_exempt
def application_form(request):

	if request.method == 'POST':
		#print(request.POST)
		var1 = IPMapping.objects.get(pincode = request.POST.get('pincode'))
		print(var1.sro_ipaddress)
		print(var1.rev_ipaddress)

		postman1 = requests.post(f'http://{var1.sro_ipaddress}:8000/apply_to_sro',data=request.POST)
		postman2 = requests.post(f'http://{var1.rev_ipaddress}:8000/apply_to_sro', data=request.POST)
		print(postman1)
		print(postman2)

		return HttpResponse(f"Data sent {postman1}  -  {postman2}")
	else:
		return render(request, 'application_form.html')