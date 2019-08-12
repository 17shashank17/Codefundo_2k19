from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate_Enrollment, Voters_Enrollment, Feedback
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Welcome</h1>")
    return render(request,"Vote/home.html")

def voter(request):
    if request.method=="POST":
        name=request.POST.get('name')
        aadhar_no=request.POST.get('aadhar')

        user=Voters_Enrollment()
        user.name=name
        user.aadhar_no=aadhar_no
        user.save()
        
        return render(request,'Vote/home.html')

    else:
        return render(request,"Vote/voter_reg.html")

def candidate(request):
    if request.method=="POST":
        name=request.POST.get('name')
        aadhar_no=request.POST.get('aadhar')

        user=Candidate_Enrollment()
        user.name=name
        user.aadhar_no=aadhar_no
        user.save()
        
        return render(request,'Vote/home.html')

    else:
        return render(request,"Vote/candidate_reg.html")

def feedback(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        subject=request.POST.get('Subject')
        message=request.POST.get('Message')

        print(name,message)

        msg=Feedback()
        msg.name=name
        msg.email=email
        msg.subject=subject
        msg.message=message
        msg.save()

        return render(request,'Vote/home.html')

    else:
        return render(request,'Vote/home.html')