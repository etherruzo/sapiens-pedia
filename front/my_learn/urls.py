from django.urls import path
from . import views

app_name = 'my_learn'

urlpatterns = [
    path('my_learn', views.my_learn, name='my_learn'),
    path('post_create', views.post_create, name='post_create'),

#    path('postsign', views.postsign, name='postsign'),
#    path('logging', views.logging, name='log'),
    #path('/postsign', views.postsign, name='postsign'),
    #path('/log', views.logout, name='log'),
]
