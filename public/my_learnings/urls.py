from django.urls import path
from . import views

app_name = 'my_learnings'

urlpatterns = [
    path('', views.my_learnings, name='my_learnings'),
    path('my_learnings', views.my_learnings, name='my_learnings'),
    path('post_create', views.post_create, name='post_create'),
#
#    path('logging', views.logging, name='log'),
    #path('/postsign', views.postsign, name='postsign'),
    #path('/log', views.logout, name='log'),
]
