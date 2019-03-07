# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Users.models import User

# Create your models here.

class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class LoanStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey("DeviceType")
    status = models.ForeignKey("DeviceStatus")

    def __str__(self):
        return self.name


class LoanRequest(models.Model):
    requester = models.ForeignKey(User)
    device = models.ForeignKey("Device")
    start_time = models.DateTimeField()
    hours = models.IntegerField()
    status = models.ForeignKey("LoanStatus",null=True)


    def end_time(self):
        return self.start_time + self.hours

