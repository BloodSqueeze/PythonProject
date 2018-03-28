from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^registration_page$', views.registration_page, name="registration_page"),
    url(r'^registration$', views.registration, name="registration"),
    url(r'^login_page$', views.login_page, name="login_page"),
    url(r'^login$', views.login, name="login"),
    url(r'^loggedin$', views.loggedin, name="loggedin"),
    url(r'^logout$', views.logout, name="logout"),
]