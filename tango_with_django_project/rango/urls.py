from django.conf.urls import patterns, url
from rango import views 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^test/', views.test, name='test'),
    url(r'^about/', views.about, name='about'))
