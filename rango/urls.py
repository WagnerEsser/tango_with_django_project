from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^question/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^question/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
)