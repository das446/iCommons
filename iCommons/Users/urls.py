from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'$', views.login),
    url(r'login/submit', views.submitLogin, name="submit_login")
]
