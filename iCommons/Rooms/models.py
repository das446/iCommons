# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Users.models import User
import datetime
import pytz

utc=pytz.UTC

# Create your models here.

RoomStatuses = (
    ("Reserved", "Reserved"),
    ("Available", "Available"),
)


class Room(models.Model):
    building = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    
    @property
    def reservations(self):
        return Reservation.objects.filter(reserved_room = self) 

    def CurReservation(self,time):
        for r in self.reservations.all():
            available = is_datetime_between(r.start_time, r.end_time, time)
            if available != "Error" and available==True:
                return r
        return None

    def Available(self, time):
        return self.CurReservation(time) == None

    def GetClass(self, time):
        r = self.CurReservation(time)
        if r==None:
            return None
        return r.cur_class

    @property
    def CurClass(self):
        return self.GetClass(datetime.datetime.now().time)

    @property
    def TestClass(self):
        return self.reservations.all()[0].cur_class

    def __str__(self):
        return self.building + " - " + self.number
        

class Class(models.Model):
    name = models.CharField(max_length=100) #full name
    course_id = models.CharField(max_length=100) #CS 265
    teachers = models.ManyToManyField(User)
    crn = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.course_id


class Reservation(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cur_class = models.ForeignKey(Class, null=True,blank=True)
    repeat = models.BooleanField(default = False)
    repeat_weeks = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=True, null=True)
    reserved_room = models.ForeignKey("Room",null=True, blank=True)

    def Description(self):
        if self.description != None and self.description != "":
            return self.description
        elif self.cur_class != None:
            teacher = self.cur_class.teachers.all()[0].full_name
            return "Occupied by "+teacher+"\nClass:"+self.cur_class.course_id 
        else:
            return ""
    
    def save(self, *args, **kwargs):
        super(Reservation,self).save(*args, **kwargs)
        if self.repeat:
            self.CreateRepeatingReservation(self.repeat_weeks, self.reserved_room)

    def CreateRepeatingReservation(self, weeks, room):
        for i in range(1,weeks+1):
            start = self.start_time + datetime.timedelta(days=7*i)
            end = self.end_time + datetime.timedelta(days=7*i)
            r = Reservation(start_time=start, end_time=end,cur_class=self.cur_class, description=self.description,repeat=False, reserved_room=room)
            r.save()

    def __str__(self):
        return self.Description() +" "+ str(self.start_time) + " to " + str(self.end_time)


def is_datetime_between(begin_time, end_time, check_time):
    try:
        begin_time = begin_time.replace(tzinfo=utc)
        end_time = end_time.replace(tzinfo=utc)
        check_time = check_time.replace(tzinfo=utc)
    except:
        return "Error"    
    return begin_time < check_time < end_time





    
