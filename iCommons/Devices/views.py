# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Device, DeviceTypes

# Create your views here.


def reserve(request):

    if request.method == 'GET':
        context = {
            "Devices": Device.objects.all(),
            "Types": DeviceTypes,
        }
        return render(request, 'reservedevice.html', context)

    if request.method == 'POST':
        t = request.POST['device']
        time = request.POST['time']
        device = Device.Ob
        LoanRequest.Create()
        return render(request, 'reservedevice.html', context)
