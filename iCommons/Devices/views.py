# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Device, DeviceType, LoanRequest, DeviceStatus
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
        device_type = get_object_or_404(DeviceType,name=device_type)
        time = int(str(request.POST['time']).split()[0])
        available = get_object_or_404(DeviceStatus, status="Available")
        device = Device.objects.filter(
            device_type=device_type, status=available).first()
        LoanRequest.objects.create(
            requester=request.user, device=device, start_time=datetime.datetime.now(), hours=time)
        return render(request, 'confirm.html')
