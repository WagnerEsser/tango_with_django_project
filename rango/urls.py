# coding:utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

from rango import views

urlpatterns  =  [
    url(r'^$', views.index, name='index'),

	# Tango Django
    url(r'^add_user$', views.add_user, name="add_user"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/', TemplateView.as_view(template_name="rango/about.html"), name='about'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^pages/', views.pages, name='pages'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page$', views.add_page, name='add_page'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^gotopage/$', views.clique_numa_pagina, name='gotopage'),
    url(r'^gotocategory/$', views.clique_numa_categoria, name='gotocategory'),
    url(r'^likecategory/$', views.curtir_uma_categoria, name='likecategory'),
    url(r'^search$', views.search, name='search'),

    # # Django Oficial
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^question/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^question/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
