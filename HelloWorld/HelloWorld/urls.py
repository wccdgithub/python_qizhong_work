"""HelloWorld URL Configuration

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
from django.conf.urls import *
from . import view,testdb,weather,hello,phone,taobao


urlpatterns = [
    url(r'^$',hello.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^weather$', weather.weatherdb),
    url(r'^phone$', phone.phonedb),
    url(r'^taobao$', taobao.taobao),
]
