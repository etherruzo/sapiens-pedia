from django.urls import path
from . import views

app_name = 'sign_in'

urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('postsign', views.postsign, name='postsign'),
#    path('logging', views.logging, name='log'),
    #path('/postsign', views.postsign, name='postsign'),
    #path('/log', views.logout, name='log'),
]
