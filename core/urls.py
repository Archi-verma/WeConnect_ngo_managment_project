"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home.views import *
urlpatterns = [
    path('',home),
    path('main/',home),
    path('form/', form ,name='form'),
    path('register/', register ,name='register'),
    path('userlogin/', userlogin ,name='userlogin'),
    path('usermain/', usermain ,name='usermain'),
    path('ngomain/',ngomain ,name='ngomain'),
    path('ngologin/', ngologin ,name='ngologin'),
    path('error/',error,name='error'),
    path('payment/',payment,name='payment'),
    path('donor/',donor,name='donor'),

    
    path('admin/', admin.site.urls),
]
