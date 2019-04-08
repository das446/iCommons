# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Rooms.models import Room
import datetime

# Create your views here.


def home(request):
    occupied_rooms = GetOccupiedRooms()
    available_rooms = GetAvailableRooms()
    context = {
        "available_rooms":available_rooms,
        "occupied_rooms":occupied_rooms
    }
    return render(request, 'home.html', context)

def GetOccupiedRooms():
    occupied_rooms = []
    rooms = Room.objects.all()
    current_time = datetime.datetime.now
    for room in rooms:
        #if room.GetClass(current_time) is not None:
        occupied_rooms.append(room)
    return occupied_rooms

def GetAvailableRooms():
    available_rooms = []
    rooms = Room.objects.all()
    current_time = datetime.datetime.now
    for room in rooms:
        if room.Available(current_time):
            available_rooms.append(room)
    return available_rooms