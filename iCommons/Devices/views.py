# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceType, LoanRequest, DeviceStatus
import datetime
import loanshark
from iCommons import settings
from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.


def reserve(request):

    if request.method == 'GET':
        context = {
            "Devices": ["Laptop","Charger"],
        }
        return render(request, 'reservedevice.html', context)

    if request.method == 'POST':
        device_type = request.POST['device']
        time = int(str(request.POST['time']).split()[0])

        device = loanshark.GetRandomDeviceOfType(device_type)

        user = request.POST['user']

        # LoanRequest.objects.create(
        #     requester=request.user, device=device, start_time=datetime.datetime.now(), hours=time)

        context = {
            "Message": "You may pick up laptop "+device +" from Rush.",
        }

        #Send confirmation email to user

        send_email(user,"Device Reservation Confirmation",context["Message"])
        notifySAs()

        return render(request, 'confirm.html', context)


def send_email(user,subject,text):
    from_email = settings.ihelp_email
    to_email = user + "@drexel.edu"
    print("from:" + from_email)
    send_mail(subject, text,from_email, [to_email], fail_silently=False) 

def notifySAs():
    print("")