from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db,auth
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

config = {
    'apiKey': "AIzaSyAN69lck26rovFU924lWgC9NOgjfVpc6cU",
    'authDomain': "sapiens-1f0c9.firebaseapp.com",
    'databaseURL': "https://sapiens-1f0c9.firebaseio.com",
    'projectId': "sapiens-1f0c9",
    'storageBucket': "sapiens-1f0c9.appspot.com",
    'messagingSenderId': "942647312753"
  }

#cred = credentials.Certificate('../../sapiens-1f0c9-firebase-adminsdk-13qhk-c3c3c2819e.json')
default_app = pyrebase.initialize_app(config)#,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
#default_app = firebase_admin.initialize_app(cred,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
auth=default_app.auth()



def my_learnings(request):

    return render(request,'my_learnings/my_learnings.html')


def post_create(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Kolkata')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))
    work = request.POST.get('work')
    progress =request.POST.get('progress')

    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    data = {
        "work":work,
        'progress':progress
    }
    database.child('users').child(a).child('reports').child(millis).set(data)
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request,'my_learnings/welcome.html', {'e':name})
