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

def sign_up(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.create_user(email=username,password=raw_password)
            current_user = username
            #return HttpResponse('Succesfully created user')
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    template = 'sign_up/sign_up.html'
    return render(request, template, context)
