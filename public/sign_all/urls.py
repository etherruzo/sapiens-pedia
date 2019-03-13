from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$',views.sign_in),
url(r'^postsign/',views.postsign),
url(r'^logout/',views.logout,name="log"),
 url(r'^sign_up/',views.sign_up,name='sign_up'),
    url(r'^postsignup/',views.postsignup,name='postsignup'),
]
