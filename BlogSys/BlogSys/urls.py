"""blogSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import *
from BlogSys.view import hello, showTime, main, hoursAhead, currentDatetime
from mailcap import show
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogSys.settings')
django.setup()


admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', main), url('^hello/$', hello), url('^time/$', showTime),
    url(r'^time/plus/(\d{1,2})/$', hoursAhead),
    url(r'^currentDatetime/$', currentDatetime)
]
