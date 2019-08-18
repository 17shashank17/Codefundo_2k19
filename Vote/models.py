from django.db import models

# Create your models here.
class Candidate_Enrollment(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    username=models.CharField(max_length=200,default="",blank=True, null=True)
    aadhar_no=models.CharField(max_length=16, blank=False,null=False,unique=True)
    candidate_aadhar_pic=models.ImageField(upload_to='images/',default="",blank=True,null=True)
    count_of_votes=models.IntegerField(default=0)
    place=models.CharField(default="",max_length=200)
    logo=models.ImageField(upload_to="images/",default="")
    candidate_pic=models.ImageField(upload_to="images/",default="")
    party=models.CharField(default="",max_length=200)

class Voters_Enrollment(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    aadhar_no=models.CharField(max_length=16, blank=False,null=False,unique=True)
    username=models.CharField(max_length=200,default="",blank=True, null=True,unique=True)
    voter_aadhar_pic=models.ImageField(upload_to='images/',default="",blank=True,null=True)
    voted=models.BooleanField(default=False)
    place=models.CharField(default="",max_length=200)
    tokens=models.CharField(default="",max_length=20)
    token_expire=models.BooleanField(default=False)
    #mobile=models.CharField(default="",max_length=10)

class Feedback(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    email=models.CharField(max_length=200,blank=True, null=True)
    subject=models.CharField(max_length=200,blank=True, null=True)
    message=models.CharField(max_length=20000,blank=True, null=True)
