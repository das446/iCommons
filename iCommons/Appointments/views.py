# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def make_appointment(request):
    context = {}
    return render(request, 'advisor.html', context)