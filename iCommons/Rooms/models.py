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

    def CurReservation(self,time):
        for reservation in self.reservations:
            if is_time_between(reservation.start_time, reservation.end_time, time):
                return reservation
        return None

    def Available(self, time):
        return self.CurReservation(time) == None

    def CurClass(self, time):
        r = self.CurReservation(time)
        if r==None:
            return None
        return r.cur_class
        

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

def is_time_between(begin_time, end_time, check_time=None):
# If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time






    
