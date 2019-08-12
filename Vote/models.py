from django.db import models

# Create your models here.
class Candidate_Enrollment(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    username=models.CharField(max_length=200,default="",blank=True, null=True)
    aadhar_no=models.CharField(max_length=16, blank=False,null=False,unique=True)
    candidate_aadhar_pic=models.ImageField(upload_to='images/',default="",blank=True,null=True)
    count_of_votes=models.IntegerField(default=0)


class Voters_Enrollment(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    aadhar_no=models.CharField(max_length=16, blank=False,null=False,unique=True)
    username=models.CharField(max_length=200,default="",blank=True, null=True)
    voter_aadhar_pic=models.ImageField(upload_to='images/',default="",blank=True,null=True)
    voted=models.BooleanField(default=False)

class Feedback(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    email=models.CharField(max_length=200,blank=True, null=True)
    subject=models.CharField(max_length=200,blank=True, null=True)
    message=models.CharField(max_length=20000,blank=True, null=True)
