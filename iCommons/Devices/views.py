# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def reserve(request):
    context = {}
    return render(request, 'reservedevice.html', context)