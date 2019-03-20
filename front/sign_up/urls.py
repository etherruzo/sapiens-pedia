from django.urls import path
from . import views

app_name = 'sign_up'

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('postsignup', views.postsignup, name='postsignup'),
    path('postsign', views.postsignup, name='postsign'),

]
