from django.db import models

# Create your models here.
class Candidate_Enrollment(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    aadhar_no=models.CharField(max_length=16, blank=False,null=False,unique=True)



class Voters_Enrollment(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    aadhar_no=models.CharField(max_length=16, blank=False,null=False,unique=True)

class Feedback(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    email=models.CharField(max_length=200,blank=True, null=True)
    subject=models.CharField(max_length=200,blank=True, null=True)
    message=models.CharField(max_length=20000,blank=True, null=True)