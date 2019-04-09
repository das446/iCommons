# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Rooms.models import Room
import datetime

# Create your views here.


def home(request):
    rooms = OrganizeRooms()
    context = {
        "available_rooms":rooms[0],
        "occupied_rooms":rooms[1]
    }
    return render(request, 'home.html', context)

def OrganizeRooms():

    organized_rooms = [[],[]] #available,unavailable
    rooms = Room.objects.all()
    current_time = datetime.datetime.now
    for room in rooms:
        if room.Available(current_time):
            organized_rooms[0].append(room)
        else:
            organized_rooms[1].append(room)

    return organized_rooms