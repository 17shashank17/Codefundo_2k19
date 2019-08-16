try: 
    from PIL import Image
except ImportError: 
    import Image

from pytesseract import image_to_string

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Candidate_Enrollment, Voters_Enrollment, Feedback
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Welcome</h1>")
    return render(request,"Vote/home.html")

def voter(request):
    if request.method=="POST":
        
        voter_aadhar_pic=request.FILES["voter_aadhar_pic"]
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
        
        username=request.POST.get('username')
        try:
            user_check=User.objects.all(username=username)
            return HttpResponse("<h1>User already exists</h1>")
        except:
            name=request.POST.get('name')
            aadhar_no=request.POST.get('aadhar')
            #voter_aadhar_pic=request.FILES["voter_aadhar_pic"]
            
            user1=Voters_Enrollment()
            user1.name=name
            user1.username=username
            user1.aadhar_no=aadhar_no
            user1.voter_aadhar_pic=voter_aadhar_pic
            user1.place=request.POST.get("state")
            user1.save()
            img=Image.open(user1.voter_aadhar_pic)
            text=image_to_string(img)
            print(text)
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
        candidate_pic=request.FILES["candidate_pic"]
        candidate_logo=request.FILES["candidate_logo"]

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
        request.session['username']=username
        user=authenticate(username=username,password=password)

        if user:
            login(request,user)
            user_info=Voters_Enrollment.objects.get(username=username)
            place=user_info.place
            candidate_info=Candidate_Enrollment.objects.filter(place=place)
            #return render(request,'Vote/profile.html',{'username':username,'user_info':user_info, 'candidate_info':candidate_info})
            return HttpResponseRedirect('/vote/profile')
            #print(username)

    else:
        return render(request,'Vote/login.html')

def profile(request):
    if request.method=="POST":
        username=request.session['username']
        voter=Voters_Enrollment.objects.get(username=username)
        name=request.POST.get("cand_name")
        token=request.POST.get("token_no")
        if token==voter.tokens:
            candidate=Candidate_Enrollment.objects.get(name=name)
            candidate.count_of_votes+=1
            print(candidate.name)
            print(candidate.count_of_votes)
            candidate.save()
            voter.voted=True
            voter.token_expire=True
            voter.save()
            return logout_user(request)      #vote is counted
        else:
            return logout_user(request)      #vote is not counted

    else:
        username=request.session['username']
        user_info=Voters_Enrollment.objects.get(username=username)
        place=user_info.place
        candidate_info=Candidate_Enrollment.objects.filter(place=place)
        return render(request,'Vote/profile.html',{'username':username,'user_info':user_info, 'candidate_info':candidate_info})
 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/vote')



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

