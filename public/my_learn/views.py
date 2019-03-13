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
    'messagingSenderId': "942647312753",
     'serviceAccount': "../sapiens-1f0c9-firebase-adminsdk-13qhk-c3c3c2819e.json"
  }

#cred = credentials.Certificate('../../sapiens-1f0c9-firebase-adminsdk-13qhk-c3c3c2819e.json')
default_app = pyrebase.initialize_app(config)#,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
#default_app = firebase_admin.initialize_app(cred,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
database=default_app.database()
auth=default_app.auth()

def getUser(req):
    idtoken= req.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    return a

#def my_learn(request):
#    return render(request,"my_learn/my_learn.html")

def my_learn(request):
    user=getUser(request)
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            tag1 = form.cleaned_data['tag1']
            tag2 = form.cleaned_data['tag2']
            tag3 = form.cleaned_data['tag3']
            learning_1 = form.cleaned_data['learning_1']
            learning_2 = form.cleaned_data['learning_2']
            learning_3 = form.cleaned_data['learning_3']
            try:
                uploadData(user,learning_1,tag1,learning_2,tag2,learning_3,tag3)
                #df_data=get_db_data(user)
                #return render_stats(df_data)
                #return HttpResponse('Succesful ')
                return redirect('my_services:my_services')

            except BadHeaderError:
                return HttpResponse('Invalid header found. ')
                #return redirect('contact_me:email_success')

    context = {'form': form}
    template = 'my_learn/my_learn.html'
    return render(request, template, context)

def uploadData(a,learning_1,tag1,learning_2,tag2,learning_3,tag3):

    h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    database.child('users').child(a).child(h).set({
                    'learning' : learning_1,
                    'tag' : tag1})
    time.sleep(1)
    h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    database.child('users').child(a).child(h).set({
                    'learning' : learning_2,
                    'tag' : tag2})
    time.sleep(1)
    h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    database.child('users').child(a).child(h).set({
                    'learning' : learning_3,
                    'tag' : tag3})


def get_db_data(a):
    def get_df(u):
	    dic_all=database.child('users').child(u).get()
	    return pd.DataFrame.from_dict(dic_all,orient='index')
    df=get_df(a)
    grouped=df.groupby('tag').count()
    return grouped


def render_stats(df):
    df.plot.pie('learning')
    # Store image in a string buffer
    buffer = BytesIO()
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pilImage.save('./my_services/static/img/my_learnings.jpg', 'JPEG')
#    pilImage.save('/Users/elena/Documents/projects/Aprendipedia/front/sapiens_front/public/my_services/static/img/my_learnings.jpg', 'JPEG')
    plt.close()
    #redirect('my_services:my_services')

    # Send buffer in a http response the the browser with the mime type image/png set
    #return HttpResponse(buffer.getvalue(), content_type="image/png")


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
    a = auth.get_account_info(idtoken)
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
    return render(request,'my_learn/welcome.html', {'e':name})
