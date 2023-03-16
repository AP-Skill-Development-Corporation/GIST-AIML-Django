from django.db import models

# Create your models here.
class Student(models.Model):
	snme = models.CharField(max_length=120)
	sage = models.IntegerField()
	semail = models.CharField(max_length=120)