

import random


from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Candidate_Enrollment, Voters_Enrollment, Feedback
from django.contrib.auth.models import User
from twilio.rest import Client
from django.core.mail import send_mail
from django.conf import settings

def send_mail_token(token):
    subject = 'Highly Secured Token'
    message = token
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['17shashank17@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

def send_token(token,mobile):
    account_sid = 'AC3cff54beeca14b3b55dc08f74fc2862d' 
    auth_token = '8de3ca4f3e5611d963d239c97ae5d406'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=token,
                                from_='+12052728298',
                                to=mobile
                            )

def home(request):
    return render(request,"Vote/home.html")

def voter(request):
    if request.method=="POST":
        
        voter_aadhar_pic=request.FILES["voter_aadhar_pic"]
        
        username=request.POST.get('username')
        try:
            user_check=User.objects.all(username=username)
            return HttpResponse("<h1>User already exists</h1>")
        except:
            name=request.POST.get('name')
            aadhar_no=request.POST.get('aadhar')
            user1=Voters_Enrollment()
            user1.name=name
            user1.username=username
            user1.aadhar_no=aadhar_no
            user1.voter_aadhar_pic=voter_aadhar_pic
            user1.place=request.POST.get("state")
            user1.save()
            user_db=User()
            user_db.username=username
            password=request.POST.get('password')
            user_db.set_password(str(password))
            user_db.email=request.POST.get('email')
            user_db.save()

            user=authenticate(username=username,password=password)
        
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
        
        return HttpResponseRedirect('/vote/profile')

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
            return HttpResponseRedirect('/vote/profile')
    else:
        return render(request,'Vote/login.html')

def get_token(aadhar,name,username,email):
    letters=aadhar+name+username+email
    token=''.join(random.choice(letters) for i in range(9))
    return token

def save_token(request):
    username=request.session['username']
    user_obj=Voters_Enrollment.objects.get(username=username)
    if user_obj.token_expire==True:
        return render(request,'Vote/token.html',{'token':'You Have Already Voted!'})
    elif len(user_obj.tokens)!=0:
        #send_mail_token(user_obj.tokens)
        return render(request,'Vote/token.html',{'token':'You Have Already Generated Token!'})
    else:
        email="17shashank17@gmail.com"
        token=get_token(user_obj.aadhar_no,user_obj.name,user_obj.username,email)
        user_obj.tokens=token
        user_obj.save()
        send_token(token,'+919632856010')
        #send_mail_token(token)
        return render(request,'Vote/token.html',{'token':token})


def profile(request):
    if request.method=="POST":
        username=request.session['username']
        print(username)
        user=User.objects.get(username=username)
        staff=False
        if user.is_staff:
            staff=True
        voter=Voters_Enrollment.objects.get(username=username)
        name=request.POST.get("cand_name")
        token=request.POST.get("token_no")
        user_info=Voters_Enrollment.objects.get(username=username)
        place=user_info.place
        candidate_info=Candidate_Enrollment.objects.filter(place=place)
        print(token)
        print(voter.tokens)
        if token==voter.tokens:
            candidate=Candidate_Enrollment.objects.get(name=name)
            candidate.count_of_votes+=1
            candidate.save()
            voter.voted=True
            voter.token_expire=True
            print(voter.token_expire)
            voter.save()
            return render(request,'Vote/done.html')      #vote is counted
        else:
            #return logout_user(request)      #vote is not counted
            return render(request,'Vote/profile.html',{'username':username,'user_info':user_info, 'candidate_info':candidate_info,'token':True,'staff':staff,})

    else:
        username=request.session['username']
        print("hi",username)
        user_info=Voters_Enrollment.objects.get(username=username)
        place=user_info.place
        candidate_info=Candidate_Enrollment.objects.filter(place=place)
        user=User.objects.get(username=username)
        staff=False
        if user.is_staff:
            staff=True
        return render(request,'Vote/profile.html',{'username':username,'user_info':user_info, 'candidate_info':candidate_info,'token':False,'staff':staff,})
 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/vote')

def result_election(request):
    place="Uttar Pradesh"
    candidate_info=Candidate_Enrollment.objects.filter(place=place)
    return render(request,'Vote/result.html',{'candidate_info':candidate_info})


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

