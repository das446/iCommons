# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ticket
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from Users.models import User
from iCommons import settings
from django.core.signing import BadSignature
from django.http import Http404


# Create your views here.
def create(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'createticket.html', context)

    else :
        subject = request.POST['subject']
        text = request.POST['text']
        email = request.POST['email']
        time = datetime.now()
        Ticket.objects.create(requester=email, subject=subject, text=text, creation_date=time, status = "new")
        send_email(email,subject,text,email)
        return render(request, 'confirm.html')

def send_email(from_email,subject,text,email):
    to_email = settings.ihelp_email
    print("from:" + from_email)
    send_mail(subject, text,from_email, [to_email], fail_silently=False) 

def view_all(request):
    context = {}
    return render(request, 'viewtickets.html', context)

def view_ticket(request, signed_pk):
    try:
      pk = Ticket.signer.unsign(signed_pk)
      ticket = Ticket.objects.get(pk=pk)
      context = {
        "Ticket":ticket
      }
      return render(request, 'viewticket.html', context)

    except (BadSignature, Ticket.DoesNotExist):
      raise Http404('Invalid ticket.')