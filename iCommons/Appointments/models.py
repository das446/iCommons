# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Users.models import User
import datetime

# Create your models here.

class Appointment(models.Model):
    student = models.ForeignKey(User, related_name = "student")
    time = models.DateTimeField()
    appointment_type = models.CharField(max_length=1000)
