from django.conf.urls import patterns, url
from rango import views
from django.views.generic import TemplateView

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
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page$', views.add_page, name='add_page'),
    url(r'^add_category/$', views.add_category, name='add_category'),

    # Django Oficial
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^question/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^question/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]