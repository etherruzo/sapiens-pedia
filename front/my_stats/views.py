from django.shortcuts import render,redirect
import pyrebase
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import image
import PIL, PIL.Image
from django.http import HttpResponse
from conf import conf
import matplotlib
matplotlib.use('TkAgg')

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


def my_stats(request):
    try:
        a,idtoken=getUserUp(request)
        df_data=get_db_data(a,idtoken)
        print(df_data['learning'])
        render_stats(df_data,a)
        context = {}
        template = 'my_stats/my_stats.html'
        #return render(request, template, context)
        return render(request,template,{"u":a})

    except Exception as e:
        return render(request,"my_learn/error.html",{"e":str(e)})


def get_db_data(local_id,token):
    dic_all=database.child('users').child(local_id).get(token)
    #df=pd.DataFrame.from_dict(dic_all.val(),orient='index')
    df0=pd.DataFrame(dic_all.val())
    df=df0.transpose()[['learning','tag']]
    grouped=df.groupby('tag').count()
    return grouped


def render_stats(df,user):
    df.plot.pie(subplots=True)
    # Store image in a string buffer
    buffer = BytesIO()
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pilImage.save('./my_stats/static/img/my_learnings.jpg', 'JPEG')
#    pilImage.save('./my_stats/static/img/my_learnings_'+str(user)+'.jpg', 'JPEG')
    plt.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    #return HttpResponse(buffer.getvalue(), content_type="image/png")
