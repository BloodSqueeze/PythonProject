from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.index),
    url(r'^(?P<id>\d+)/browse$', views.browse),
    url(r'^(?P<id>\d+)/playlists$', views.playlists),
]