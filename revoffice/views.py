from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha256
from datetime import datetime
import json
import requests

class Blockchain:

	def __init__(self):
		self.ledger = []
		self.BlockQueue = []
		with open('revoffice/local_ledger.json') as local_ledger:
			self.ledger = json.load(local_ledger)
		print("Blockchain Initiated!")
	
	def get_prev_hash(self):
		if len(self.ledger['chain']) == 0:
			return '0'
		else:
			return self.compute_hash(self.ledger['chain'][-1])
	#print(self.ledger['chain'][-1])

	def create_block(self, timestamp, survey_no, pincode, PrevOwner_fname, PrevOwner_mname, PrevOwner_lname, PrevOwner_adhaarno, NewOwner_fname, NewOwner_mname, NewOwner_lname,NewOwner_adhaarno,TransactionNote):
		prev_hash = self.get_prev_hash()
		block = {'index': str(len(self.ledger['chain']) + 1),
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

	def compute_hash(self,block):
		encoded_block = json.dumps(block).encode()
		return sha256(encoded_block).hexdigest()

#no validation will be done inthis function... al the validation is done in 
#blockchain_ladle
#ladle is vessel used to carry molten gold
	def append_block_into_ledger(self, block):

		self.ledger['chain'].append(block)	#till here block and ele of ledger['chain'] are dict
		print(self.ledger)
		with open('revoffice/local_ledger.json','w') as local_ledger:
				json.dump(self.ledger, local_ledger,indent=4)
		print("wrote into local ledger at rev")

	def search_block(self, survey_no):
		topla = []
		for block in self.ledger['chain']:
			if block['survey_no'] == survey_no:
				print("Found \n\n")
				topla.append(block)

		return topla


blockchain = Blockchain()




@csrf_exempt
def search_land_details(request):
	if request.method == "POST":
		print("DEBUG @rev_views. search_land_details\n")
		print(request.POST)
		topla = blockchain.search_block(request.POST.get('propertyno'))
		print(topla)

		if(len(topla) == 0):
			return HttpResponse("Details Not available: (TODO: Right the reasons here, and add return to homepage button)");
		else:
			return render(request, 'display_land_details.html', {'topla':topla})

	else:
		return render(request, 'search_land_details.html')


def rev_homepage(request):
	return render(request, 'rev_homepage.html')


def search_land_details(request):
	return render(request, 'search_land_details.html')


@csrf_exempt
def append_the_ledger(request):
	print(request.GET)
	print(request.POST)

	molten_block = blockchain.create_block(
		request.POST['timestamp'],
		request.POST['survey_no'],
		request.POST['pincode'],
		request.POST['PreviousOwner_fname'],
		request.POST['PreviousOwner_mname'],
		request.POST['PreviousOwner_lname'],
		request.POST['PreviousOwner_adhaarno'],
		request.POST['NewOwner_fname'],
		request.POST['NewOwner_mname'],
		request.POST['NewOwner_lname'],
		request.POST['NewOwner_adhaarno'],
		request.POST['TransactionNote']
		)

	molten_block =json.dumps(molten_block).encode()
	molten_block = json.loads(molten_block)
	blockchain.append_block_into_ledger(molten_block)
	print("DEBUG: @append_the_ledger -->cS ")
	print("ledger updated")
	return



@csrf_exempt
def get_block_at_rev(request):
	print(request.POST)
	temp_block = blockchain.create_block(
		request.POST['timestamp'],
		request.POST['survey_no'],
		request.POST['pincode'],
		request.POST['PreviousOwner_fname'],
		request.POST['PreviousOwner_mname'],
		request.POST['PreviousOwner_lname'],
		request.POST['PreviousOwner_adhaarno'],
		request.POST['NewOwner_fname'],
		request.POST['NewOwner_mname'],
		request.POST['NewOwner_lname'],
		request.POST['NewOwner_adhaarno'],
		request.POST['TransactionNote']
		)
	temp_json_block = json.dumps(temp_block).encode()
	blockchain.BlockQueue.append(temp_json_block)
	print(blockchain.BlockQueue)
	print(type(temp_json_block))
	print("Received data at revenue department")
	return


def print_BlockQueue(request):
	tempblocks = []
	for temp_block in blockchain.BlockQueue:
		tempblocks.append(json.loads(temp_block.decode('utf-8')))

	print(type(tempblocks))
	#print(tempblocks)

	return render(request,"index.html",{'all_applications':tempblocks})

	#return render(request,"display_pending_blocks.html",{'all_applications':tempblocks})

def get_top_hash(request):
	hash = blockchain.get_prev_hash()
	#print(hash)
	hash = json.dumps(hash)
	return HttpResponse(hash)



def blockchain_ladle(request):
	print("@ revoffice.views -> blockchain_ladle")
#	print(request.GET['survey_no'])
#	return HttpResponse(request.GET)
	
	response_cs = requests.get('http://127.0.0.1:8000/get_top_hash')
	response_sro = requests.get('http://127.0.105.1:8000/get_top_hash')
	response_rev = requests.get('http://127.0.105.2:8000/get_top_hash')
	print("Collected all hash's")

	print("Top hash from CS: " + str(response_cs.content))
	print("Top hash form SRO: " + str(response_sro.content))
	print("Top hash from rev: " + str(response_rev.content))

	## if all hash same
	if (response_cs.content == response_sro.content and response_sro.content == response_rev.content):
		#append block in self.ledger
		molten_block = blockchain.create_block(
		str(datetime.now()),
		request.GET['survey_no'],
		request.GET['pincode'],
		request.GET['PreviousOwner_fname'],
		request.GET['PreviousOwner_mname'],
		request.GET['PreviousOwner_lname'],
		request.GET['PreviousOwner_adhaarno'],
		request.GET['NewOwner_fname'],
		request.GET['NewOwner_mname'],
		request.GET['NewOwner_lname'],
		request.GET['NewOwner_adhaarno'],
		request.GET['TransactionNote']
		)

		molten_block =json.dumps(molten_block).encode()
		#print("@ladle")
		#print(type(molten_block))
		#print()
		molten_block = json.loads(molten_block)
		#add to self.ledger
		blockchain.append_block_into_ledger(molten_block)

	
		#send block and call append in sro's ledger
		res1 = requests.post('http://127.0.0.1:8000/append_the_ledger',data=molten_block)
		print("Response for sending block to CS")
		#print(res1)
		#send block and call append in rev's ledger
		res2 = requests.post('http://127.0.105.1:8000/append_the_ledger', data=molten_block)
		print("Response from sending block to SRO")
		#print(res2)
	else:

		return HttpResponse("Hash Did not matched... Ledger is inconsistent.. (task- 13.2create page)")
	#return HttpResponse(response_cs)
	return render(request, 'rev_homepage.html')
