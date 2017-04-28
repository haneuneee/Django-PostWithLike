from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.addPost, name='addPost'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/rate/$', views.ratePost, name='ratePost')
]