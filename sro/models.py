from django.db import models
import datetime
# Create your models here.
class ApplicationQueue(models.Model):
	applicants_firstname	= models.CharField(max_length=50)
	applicants_middlename	= models.CharField(max_length=50)
	applicants_lastname		= models.CharField(max_length=60)
	applicants_mobno		= models.CharField(max_length=12)
	applicants_adharno		= models.CharField(max_length=12)
	survey_no				= models.CharField(max_length=30)
	timestamp				= models.DateTimeField(default=datetime.datetime.now)
