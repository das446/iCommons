from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'account', views.view_account, name="account"),
    url(r'$', views.Login, name="login")
]
