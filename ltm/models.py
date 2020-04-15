from django.db import models

class IPMapping(models.Model):
	pincode = models.CharField(max_length=9)
	ipaddress = models.GenericIPAddressField()