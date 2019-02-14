# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ticket
import datetime

# Create your views here.
def create(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'createticket.html', context)

    else :
        user = request.user.username
        subject = request.POST['subject']
        text = request.POST['text']
        time = datetime.now()
        return render(request, 'confirm.html')
        

def view_all(request):
    context = {}
    return render(request, 'viewtickets.html', context)