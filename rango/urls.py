from django.conf.urls import patterns, url
from rango import views

# ====== TESTE ====== #
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
	
	# Tango Django
	# url(r'^about/', views.about, name='about'),
    # utilizando a view genérica abaixo (TemplateView), ele chama o template direto (template_name="rango/about.html"),
    # não precisando criar nossa própria view, pois a view que gerará o template 'about.html' não precisa de nenhum cálculo
    # específico, só precisa renderizar o template 'about.html'
    url(r'^about/', TemplateView.as_view(template_name="rango/about.html"), name='about'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),

    # Django Oficial
    url(r'^question/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^question/(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^question/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

)