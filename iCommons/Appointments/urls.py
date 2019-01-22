from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'create', views.make_appointment, name="make_appointment"),
]
