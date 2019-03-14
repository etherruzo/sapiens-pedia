from django.shortcuts import render,redirect
import pyrebase
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import image
import PIL, PIL.Image
from django.http import HttpResponse

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


def getUserUp(req):
    idtoken= req.session['uid']
    a = auth.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    return a,idtoken


def my_services(request):
    a,idtoken=getUserUp(request)
    df_data=get_db_data(a,idtoken)
    render_stats(df_data,a)
    context = {}
    template = 'my_services/my_services.html'
    return render(request, template, context)



def my_services1(request):
    try:
        user,token=getUserUp(request)
        df_data=get_db_data(user,token,database)
        render_stats(df_data)
        context = {}
        template = 'my_services/my_services.html'
        return render(request, template, context)
    except:
        return render(request,"my_services/error.html")


def get_db_data(local_id,token):
    dic_all=database.child('users').child(local_id).get(token)
    #df=pd.DataFrame.from_dict(dic_all.val(),orient='index')
    df0=pd.DataFrame(dic_all.val())
    df=df0.transpose()[['learning','tag']]
    grouped=df.groupby('tag').count()
    return grouped


def render_stats(df,user):
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
