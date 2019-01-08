# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def login(request):
    context = {}
    return render(request, 'Users/login.html', context)

def submitLogin(request):
    context = {}
    return render(request, 'Users/login.html', context)
