from django.db import models

class IPMapping(models.Model):
	pincode = models.CharField(max_length=9)
	sro_ipaddress = models.GenericIPAddressField()
	rev_ipaddress = models.GenericIPAddressField()