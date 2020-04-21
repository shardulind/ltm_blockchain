from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ApplicationQueue
from umbra.models import IPMapping
from .forms import BlockForm
from datetime import datetime
import requests
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


def create_block( timestamp, survey_no, pincode, PrevOwner_fname, PrevOwner_mname, PrevOwner_lname, PrevOwner_adhaarno, NewOwner_fname, NewOwner_mname, NewOwner_lname,NewOwner_adhaarno,TransactionNote):
	prev_hash = '0'
	block = {'index': '1',
			 'previous_hash' : prev_hash,
			 'timestamp': str(timestamp),
			 'survey_no': survey_no,
			 'pincode': pincode,
			 'PreviousOwner_fname' : PrevOwner_fname,
			 'PreviousOwner_mname' : PrevOwner_mname,
			 'PreviousOwner_lname' : PrevOwner_lname,
			 'PreviousOwner_adhaarno': PrevOwner_adhaarno,
			 'NewOwner_fname': NewOwner_fname,
			 'NewOwner_mname': NewOwner_mname,
			 'NewOwner_lname': NewOwner_lname,
			 'NewOwner_adhaarno':NewOwner_adhaarno,
			 'TransactionNote': TransactionNote
	}
	return block;




def send_appn_to_rev(request):
	print(request.POST)
	print(request.GET)


	temp_block = create_block(
		datetime.now(), 
		request.GET['survey_no'], 
		request.POST['pincode'], 
		request.POST['previous_owner_fname'],
		request.POST['previous_owner_mname'], 
		request.POST['previous_owner_lname'], 
		request.POST['previous_owner_adharno'],
		request.GET['newowner_fname'], 
		request.GET['newowner_mname'], 
		request.GET['newowner_lname'],
		request.GET['newowner_adharno'],
		request.POST['transaction_note'])
	#print(temp_block)
	rev_ip = IPMapping.objects.get(pincode=request.POST['pincode'])
	
	res = requests.post(f'http://{rev_ip.rev_ipaddress}:8000/get_tempblock_at_rev',data=temp_block)


	return HttpResponse("baghut")

@csrf_exempt
def process_application(request):
	print(request.GET)
	application = ApplicationQueue.objects.get(id = request.GET['obj_id'])
	print(application)

	form = BlockForm()

	return render(request, 'process_appn.html', {'form':form,'application':application,'obj_id':request.GET['obj_id']})