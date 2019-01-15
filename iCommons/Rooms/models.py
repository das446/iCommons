# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Users.models import User

# Create your models here.

class Room(models.Model):
    building = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    cur_class = models.CharField(max_length=100)
    cur_teacher = models.ForeignKey(User)

class ReservationRequest(models.Model):
    room = models.ForeignKey(Room)
    start_time = models.DateTimeField()
    hours = models.IntegerField()