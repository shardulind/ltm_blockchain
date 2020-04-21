from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ApplicationQueue
from .forms import BlockForm

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


# rendering function to display pending application letters.
def display_pending_applicaitons(request):
	topla = ApplicationQueue.objects.values()
	#print(topla)
	
	return render(request, 'display_appn.html', {'all_applications':topla})

def send_appn_to_rev(request):
	print(request.POST)
	print(request.GET)
	return HttpResponse("Success")

def process_application(request):
	print(request.GET)
	application = ApplicationQueue.objects.get(id = request.GET['obj_id'])
	print(application)

	form = BlockForm()

	return render(request, 'process_appn.html', {'form':form,'application':application,'obj_id':request.GET['obj_id']})