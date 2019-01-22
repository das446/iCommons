# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Users.models import User

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class LoanRequest(models.Model):
    requester = models.ForeignKey(User)
    device = models.ForeignKey(Device)
    start_time = models.DateTimeField()
    hours = models.IntegerField()

    def end_time(self):
        return self.start_time + self.hours
