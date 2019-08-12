'''try: 
    from PIL import Image
except ImportError: 
    import Image

import pytesseract'''

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Candidate_Enrollment, Voters_Enrollment, Feedback
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Welcome</h1>")
    return render(request,"Vote/home.html")

def voter(request):
    if request.method=="POST":
        

        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

        #text=pytesseract.image_to_string(Image.open(voter_aadhar_pic))
        #print(text)
        
        username=request.POST.get('username')
        try:
            user_check=User.objects.all(username=username)
            return HttpResponse("<h1>User already exists</h1>")
        except:
            name=request.POST.get('name')
            aadhar_no=request.POST.get('aadhar')
            voter_aadhar_pic=request.FILES["voter_aadhar_pic"]
            
            user=Voters_Enrollment()
            user.name=name
            user.username=username
            user.aadhar_no=aadhar_no
            user.voter_aadhar_pic=voter_aadhar_pic
            user.save()
            
            user_db=User()
            user_db.username=username
            password=request.POST.get('password')
            user_db.set_password(str(password))
            user_db.email=request.POST.get('email')
            user_db.save()

            user=authenticate(username=username,password=password)
            login(request,user)
        
        return render(request,'Vote/login.html')

    else:
        return render(request,"Vote/voter_reg.html")

def candidate(request):
    if request.method=="POST":
        name=request.POST.get('name')
        aadhar_no=request.POST.get('aadhar')
        candidate_aadhar_pic=request.FILES["candidate_aadhar_pic"]

        user=Candidate_Enrollment()
        user.name=name
        user.aadhar_no=aadhar_no
        user.candidate_aadhar_pic=candidate_aadhar_pic
        user.save()
        
        return render(request,'Vote/home.html')

    else:
        return render(request,"Vote/candidate_reg.html")

def login_user(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            user_info=Voters_Enrollment.objects.get(username=username)
            print(user_info.voted)
            return render(request,'Vote/profile.html',{'username':username,'user_info':user_info})

    else:
        return render(request,'Vote/login.html')

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

