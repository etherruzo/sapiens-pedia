from django.urls import path
from . import views

app_name = 'my_stats'

urlpatterns = [
    path('', views.my_stats, name='my_stats')
]