from django.shortcuts import render

# Create your views here.
from hashlib import sha256
import json


class Blockchain:

	def __init__(self):
		self.chain = []

	def get_prev_hash(self):
		if len(self.chain) == 0:
			return '0'
		else:
			return self.compute_hash(self.chain[-1])


	def create_block(self, timestamp, survey_no, pincode, PrevOwner_fname, PrevOwner_mname, PrevOwner_lname, PrevOwner_adhaarno, NewOwner_fname, NewOwner_mname, NewOwner_lname,NewOwner_adhaarno,TransactionNote):
		prev_hash = self.get_prev_hash()
		block = {'index': len(self.chain) + 1,
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

blockchain = Blockchain()


def get_block_at_rev(request):
	print(request)
	