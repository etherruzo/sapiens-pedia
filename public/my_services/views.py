from django.shortcuts import render,redirect
import pyrebase
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import image
import PIL, PIL.Image

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
    return a,idtoken


def my_services(request):
    try:
        user,token=getUserUp(request)
        df_data=get_db_data(user,token,database)
        render_stats(df_data)
        context = {}
        template = 'my_services/my_services.html'
        return render(request, template, context)
    except:
        return render(request,"my_services/error.html")


def get_db_data(a,token,db):
    local_id=auth.get_account_info(token)['users'][0]['localId']
    dic_all=db.child('users').child(local_id).get(token)
    df=pd.DataFrame.from_dict(dic_all.val(),orient='index')
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
