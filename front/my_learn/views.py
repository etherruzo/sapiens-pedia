from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
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
database=default_app.database()
auth=default_app.auth()

def getUser(req):
    idtoken= req.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    return a


def getUserUp(req):
    idtoken= req.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    return a,idtoken

def my_learn2(request):
    user,token=getUserUp(request)
    public1=request.POST.get("public1")
    public2=request.POST.get("public2")
    public3=request.POST.get("public3")
    tag1=request.POST.get("tag1")
    tag2=request.POST.get("tag2")
    tag3=request.POST.get("tag2")
    learning_1=request.POST.get("learning_1")
    learning_2=request.POST.get("learning_2")
    learning_3=request.POST.get("learning_3")
    uploadData(user,token,"learning_1","tag1","public1","learning_2","public2","tag2","learning_3","tag3","public3")
    try:
        return redirect('my_stats:my_stats')

    except BadHeaderError:
        return HttpResponse('Invalid header found. ')

    context = {'form': form}
    template = 'my_learn/my_learn.html'
    return render(request, template, context)

def my_learn1(request):

    try:
        user,token=getUserUp(request)
    except Exception as e:
        return render(request,"my_learn/error.html",{"e":str(e)})


    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        template = 'my_learn/my_learn.html'
        return render(request, template, context)
    else:
        form = ContactForm(request.POST)
        uploadData(user,token,"learning_1","tag1","public1","learning_2","public2","tag2","learning_3","tag3","public3")

        public1=request.POST.get("public1")
        public2=request.POST.get("public2")
        public3=request.POST.get("public3")
        tag1=request.POST.get("tag1")
        tag2=request.POST.get("tag2")
        tag3=request.POST.get("tag3")
        learning_1=request.POST.get("learning_1")
        learning_2=request.POST.get("learning_2")
        learning_3=request.POST.get("learning_3")
        uploadData(user,token,learning_1,tag1,public1,learning_2,public2,tag2,learning_3,tag3,public3)

        if form.is_valid(): #TODO

            public1 = False #form.cleaned_data['public1']
            public2 = False #form.cleaned_data['public2']
            public3 = False #form.cleaned_data['public3']
            tag1 = form.cleaned_data['tag1']
            tag2 = form.cleaned_data['tag2']
            tag3 = form.cleaned_data['tag3']
            learning_1 = form.cleaned_data['learning_1']
            learning_2 = form.cleaned_data['learning_2']
            learning_3 = form.cleaned_data['learning_3']
            uploadData(user,token,"learning_1","tag1","public1","learning_2","public2","tag2","learning_3","tag3","public3")

            try:
                uploadData(user,token,learning_1,tag1,public1,learning_2,public2,tag2,learning_3,tag3,public3)
                return redirect('my_stats:my_stats')

            except BadHeaderError:
                return HttpResponse('Invalid header found. ')

        context = {'form': form}
        template = 'my_stats/my_stats.html'
        return render(request, template, context)

def get_boolean_from_request(request, key, method='POST'):
	" gets the value from request and returns it's boolean state "
	value = getattr(request, method).get(key, False)

	if value == 'False' or value == 'false' or value == '0' or value == 0:
		value = False
	elif value:
		value = True
	else:
		value = False

	return value

def my_learn(request):

    try:
        user,token=getUserUp(request)
    except Exception as e:
        return render(request,"my_learn/error.html",{"e":str(e)})

    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        template = 'my_learn/my_learn.html'
        return render(request, template, context)
    else:
        form = ContactForm(request.POST)
        public1=get_boolean_from_request(request,"public1")
        public2=get_boolean_from_request(request,"public2")
        public3=get_boolean_from_request(request,"public3")
        tag1=request.POST.get("tag1")
        tag2=request.POST.get("tag2")
        tag3=request.POST.get("tag3")
        learning_1=request.POST.get("learning_1")
        learning_2=request.POST.get("learning_2")
        learning_3=request.POST.get("learning_3")
        try:
            uploadData(user,token,learning_1,tag1,public1,learning_2,tag2,public2,learning_3,tag3,public3)


            return redirect('my_stats:my_stats')

        except BadHeaderError:
            return HttpResponse('Invalid header found. ')

        context = {'form': form}
        template = 'my_stats/my_stats.html'
        return render(request, template, context)


def my_learn0(request):

    try:
        user,token=getUserUp(request)
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                public1 = form.cleaned_data['public1']
                public2 = form.cleaned_data['public2']
                public3 = form.cleaned_data['public3']
                tag1 = form.cleaned_data['tag1']
                tag2 = form.cleaned_data['tag2']
                tag3 = form.cleaned_data['tag3']
                learning_1 = form.cleaned_data['learning_1']
                learning_2 = form.cleaned_data['learning_2']
                learning_3 = form.cleaned_data['learning_3']

                try:
                    uploadData(user,token,learning_1,tag1,public1,learning_2,public2,tag2,learning_3,tag3,public3)
                    return redirect('my_stats:my_stats')

                except BadHeaderError:
                    return HttpResponse('Invalid header found. ')

        context = {'form': form}
        template = 'my_learn/my_learn.html'
        return render(request, template, context)
    except:
        return render(request,"sign_in/sign_in.html")


def uploadData(a,tok,learning_1,tag1,public1,learning_2,tag2,public2,learning_3,tag3,public3):

    h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    database.child('users').child(a).child(h).set({
                    'learning' : learning_1,
                    'tag' : tag1,
                    'public' : public1},tok)
    time.sleep(1)
    h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    database.child('users').child(a).child(h).set({
                    'learning' : learning_2,
                    'tag' : tag2,
                    'public' : public2},tok)
    time.sleep(1)
    h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    database.child('users').child(a).child(h).set({
                    'learning' : learning_3,
                    'tag' : tag3,
                    'public' : public3},tok)



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
