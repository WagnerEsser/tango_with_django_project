# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from rango import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls', namespace="rango")),
    url(r'^$', views.index, name='index'),
]
