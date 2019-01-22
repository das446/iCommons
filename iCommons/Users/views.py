# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def login(request):
    context = {}
    return render(request, 'login.html', context)

def view_account(request):
    context = {}
    return render(request, 'account.html', context)
