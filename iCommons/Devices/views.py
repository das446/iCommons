# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceType, LoanRequest, DeviceStatus
import datetime
import loanshark

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

        # LoanRequest.objects.create(
        #     requester=request.user, device=device, start_time=datetime.datetime.now(), hours=time)

        context = {
            "Message": "You may pick up laptop "+device +" from Rush.",
        }
        return render(request, 'confirm.html', context)
