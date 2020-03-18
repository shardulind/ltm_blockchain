from django.db import models

# Create your models here.
class SROMapping(models.Model):
	pincode = models.IntegerField()
	ip_address = models.GenericIPAddressField()

