# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ticket
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from Users.models import User

# Create your views here.
def create(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'createticket.html', context)

    else :
        username = request.user.username
        subject = request.POST['subject']
        text = request.POST['text']
        time = datetime.now()
        user = User.objects.get(username=username)
        Ticket.objects.create(requester=user, subject=subject, text=text, creation_date=time, status = "new")
        send_email(user,subject,text)
        return render(request, 'confirm.html')

def send_email(user,subject,text):
    to_email = "ihelp@drexel.edu"
    from_email = user.email
    print("from:" + from_email)
    send_mail(subject, text,from_email, [to_email], fail_silently=False) 

def view_all(request):
    context = {}
    return render(request, 'viewtickets.html', context)