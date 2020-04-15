from django.shortcuts import render
from firebase_admin import db,auth,credentials
import firebase_admin

def home(request):
    context = {}
    template = 'home/home.html'
#    global default_app
#    cred = credentials.Certificate('/Users/elena/Documents/Projects/sapiens-pedia/sapiens-1f0c9-firebase-adminsdk-13qhk-c3c3c2819e.json')
#    try:
#        default_app = firebase_admin.initialize_app(cred,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})
#        database = default_app.database()
#        auth = default_app.auth()
#    except:
#        pass
#    default_app = firebase_admin.initialize_app(cred,options={'databaseURL': 'https://sapiens-1f0c9.firebaseio.com/'})


    return render(request, template, context)
