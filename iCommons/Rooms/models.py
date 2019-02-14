# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Users.models import User

# Create your models here.

RoomStatuses = (
    ("Reserved", "Reserved"),
    ("Available", "Available"),
)


class Room(models.Model):
    building = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    cur_class = models.CharField(max_length=100)
    cur_teacher = models.ForeignKey(User)
    reservations = models.ManyToManyField("Reservation")

    def available(self, time):
        return True


class Reservation(models.Model):
    start_time = models.DateTimeField()
    hours = models.IntegerField()

