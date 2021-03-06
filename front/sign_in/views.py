from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db,auth
import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import image
import PIL, PIL.Image
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import pyrebase
from conf import conf

config=conf.config
default_app = pyrebase.initialize_app(config)#,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
auth=default_app.auth()



def sign_in(request):
    return render(request,"sign_in/sign_in.html")

def postsign(request):
    email=request.POST.get("email")
    passw=request.POST.get("pass")
    try:
        user=auth.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request,"sign_in/sign_in.html",{"messg":message})
    #return render(request,"welcome",{"e":email})
    print(user)
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"sign_in/welcome.html",{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'sign_in/sign_in.html')
