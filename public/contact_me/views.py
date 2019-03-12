from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

import firebase_admin
from firebase_admin import db,auth,credentials
import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO
import image
import PIL, PIL.Image


def get_db_data(user,root):
    root = db.reference()
    def get_df(u):
	    dic_all=root.child(u).get()
	    return pd.DataFrame.from_dict(dic_all,orient='index')
    df=get_df(user.uid)
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
    pilImage.save('/Users/elena/Documents/projects/Aprendipedia/front/sapiens_front/public/my_services/static/img/my_learnings.jpg', 'JPEG')
    plt.close()
    #redirect('my_services:my_services')

    # Send buffer in a http response the the browser with the mime type image/png set
    #return HttpResponse(buffer.getvalue(), content_type="image/png")

def uploadData(learning_1,tag1,learning_2,tag2,learning_3,tag3):
    try:
        user_name="etomasherruzo@gmail.com"
        cred = credentials.Certificate('/Users/elena/Documents/projects/Aprendipedia/firebase/sapiens-1f0c9-firebase-adminsdk-13qhk-c3c3c2819e.json')
        default_app = firebase_admin.initialize_app(cred,options={
                    'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
        user = auth.get_user_by_email(user_name)
        print('Successfully fetched user data: {0}'.format(user.uid))
        root = db.reference()

        h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
        root.child(user.uid).child(h).set({
                    'learning' : learning_1,
                    'tag' : tag1})
        time.sleep(1)
        h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
        root.child(user.uid).child(h).set({
                    'learning' : learning_2,
                    'tag' : tag2})
        time.sleep(1)
        h=datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
        root.child(user.uid).child(h).set({
                    'learning' : learning_3,
                    'tag' : tag3})
        return user,root
    except:
        print("No user record found for the provided email")


def contact_me(request):
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
                user,root=uploadData(learning_1,tag1,learning_2,tag2,learning_3,tag3)
                df_data=get_db_data(user,root)
                return render_stats(df_data)

            except BadHeaderError:
                return HttpResponse('Invalid header found. ')
                #return redirect('contact_me:email_success')

    context = {'form': form}
    template = 'contact_me/contact_me.html'
    return render(request, template, context)


def email_success(request):
    context = {}
    template = 'contact_me/email_success.html'
    return render(request, template, context)
