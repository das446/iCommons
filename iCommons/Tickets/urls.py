from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'create', views.create, name="create"),
    url(r'view', views.view_all, name="view")
]
