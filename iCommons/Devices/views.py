# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Device, DeviceType, LoanRequest
import datetime

# Create your views here.


def reserve(request):

    if request.method == 'GET':
        context = {
            "Devices": Device.objects.all(),
            "Types": DeviceType.objects.all(),
        }
        return render(request, 'reservedevice.html', context)

    if request.method == 'POST':
        device_type = request.POST['device']
        time = int(str(request.POST['time']).split()[0])
        device = Device.objects.filter(
            device_type=device_type, status="Available").first()
        LoanRequest.objects.create(
            requester=request.user, device=device, start_time=datetime.datetime.now(), hours=time)
        return render(request, 'confirm.html')
