# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def reserve(request):
    context = {}
    return render(request, 'reserveroom.html', context)

def outlook(request):
    context = {}
    return render(request, 'outlooktest.html', context)

def view_available(request):
    context = {}
    return render(request, 'ClassAvailable.html', context)