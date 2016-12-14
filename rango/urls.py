# coding:utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

from rango import views
from rango.views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', TemplateView.as_view(template_name="rango/about.html"), name='about'),

    ## USER ##
    url(r'^add_user$', views.AddUser, name="add_user"),
    url(r'^register/$', views.Register, name='register'),
    url(r'^login/$', views.UserLogin, name='login'),
    url(r'^restricted/$', login_required(TemplateView.as_view(template_name="rango/restricted.html")), name='restricted'),
    url(r'^logout/$', views.UserLogout, name='logout'),

    ## CATEGORY ##
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.ShowCategory, name='category'),
    url(r'^category/$', views.GoToCategory, name='gotocategory'),
    url(r'^cad/category/$', CategoryView.as_view(), name='cad_category'),
    url(r'^edita/category/(?P<id>[0-9]+)/$', CategoryView.as_view(), name='edita_category'),
    url(r'^deleta/category/(?P<id>[0-9]+)/$', views.CategoryDelete, name='deleta_category'),
    url(r'^categories/', views.ListCategories, name='categories'),
    url(r'^likecategory/$', views.LikeCategory, name='likecategory'),

    ## PAGE ##
    url(r'^category/(?P<category_name_slug>[\w\-]+)/cad/page/$', PageView.as_view(), name='cad_page'),
    url(r'^edita/page/(?P<id>[0-9]+)/$', PageView.as_view(), name='edita_page'),
    url(r'^deleta/page/(?P<id>[0-9]+)/$', views.PageDelete, name='deleta_page'),
    url(r'^page/$', views.GoToPage, name='gotopage'),
    url(r'^pages/', views.Pages, name='pages'),
    url(r'^search$', views.Search, name='search'),

    ## DJANGO OFICIAL ##
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^question/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^question/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
