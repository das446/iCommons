from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'reserve', views.reserve, name="reserve"),
    url(r'outlook', views.outlook, name="outlook"),
    url(r'view_available', views.view_available, name="view_available"),
]
