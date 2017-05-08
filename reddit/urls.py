from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='reddit:index')),
    url(r'^index/$', views.index, name='index'),
    url(r'^add/$', views.addPost, name='addPost'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/rate/$', views.ratePost, name='ratePost'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.deletePost, name='deletePost'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.editPost, name='editPost'),
    url(r'^(?P<pk>[0-9]+)/comment/$', views.addComment, name='addComment'),
    url(r'^comment/(?P<pk>[0-9]+)/edit/$', views.editComment, name='editComment'),
    url(r'^comment/(?P<pk>[0-9]+)/delete/$', views.deleteComment, name='deleteComment'),
    url(r'^comment/(?P<pk>[0-9]+)/reply/$', views.addReply, name='addReply'),
]