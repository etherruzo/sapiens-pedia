"""CV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('my_stats/', include('my_stats.urls', namespace='my_stats')),
    #path('sign_in/logging/', include('sign_in.urls', namespace='sign_in')),
    #path('sign_in/postsign/', include('sign_in.urls', namespace='sign_in')),
    #path('sign_up/postsignup/', include('sign_up.urls', namespace='sign_up')),
    #path('sign_all/', include('sign_all.urls', namespace='sign_all')),
    path('my_learn/', include('my_learn.urls', namespace='my_learn')),
    path('sign_in/', include('sign_in.urls', namespace='sign_in')),
    path('sign_up/', include('sign_up.urls', namespace='sign_up')),
    path('admin/', admin.site.urls),
]
