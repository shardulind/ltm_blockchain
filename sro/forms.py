from django import forms

class BlockForm(forms.Form):
	#application_id = forms.CharField()
	previous_owner_fname = forms.CharField(label="Owners First Name")
	previous_owner_mname = forms.CharField(label="Owners Middle Name")
	previous_owner_lname = forms.CharField(label="Owners Last Name")
	previous_owner_adharno = forms.CharField(label="Owners Aadhar Number")
	transaction_note = forms.CharField(label="Note", widget=forms.Textarea	)
