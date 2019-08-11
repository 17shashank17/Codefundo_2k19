from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate_Enrollment, Voters_Enrollment
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