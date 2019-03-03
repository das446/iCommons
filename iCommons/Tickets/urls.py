from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'create', views.create, name="create"),
    url(r'view', views.view_all, name="view_all"),
    url(r'view/(?P<signed_pk>[0-9]+/[A-Za-z0-9_=-]+)/$', views.view_ticket, name='view_ticket')
]
