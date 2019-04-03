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
    reservations = models.ManyToManyField("Reservation")

    def Available(self, time):
        return True

    def CurClass(self, time):
        return None

class Class(models.Model):
    name = models.CharField(max_length=100) #full name
    course_id = models.CharField(max_length=10) #CS 265
    teacher = models.ForeignKey(User)


class Reservation(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cur_class = models.ForeignKey(Class, null=True,blank=True)
    repeat = models.BooleanField(default = False)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def Description(self):
        if self.description != None and self.description != "":
            return self.description
        elif self.cur_class != None:
            teacher = self.cur_class.teacher.FullName()
            return "Occupied by "+teacher+"\nClass:"+self.cur_class.course_id 
        else:
            return ""






    
