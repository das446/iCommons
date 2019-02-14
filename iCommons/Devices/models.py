# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Users.models import User

# Create your models here.

DeviceTypes = (
    ("Laptop", "Laptop"),
    ("Charger", "Charger"),
    ("HDMI", "HDMI"),
)

DeviceStatuses = (
    ("Reserved", "Reserved"),
    ("Loaned Out", "Loaned Out"),
    ("Available", "Available"),
)

LoanStatuses = (
    ("Awaiting Pickup", "Awaiting Pickup"),
    ("Loaned Out", "Loaned Out"),
    ("Returned", "Returned"),
)

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100, choices = DeviceTypes)
    status = models.CharField(max_length=100, choices = DeviceStatuses)


class LoanRequest(models.Model):
    requester = models.ForeignKey(User)
    device = models.ForeignKey(Device)
    start_time = models.DateTimeField()
    hours = models.IntegerField()


    def end_time(self):
        return self.start_time + self.hours
