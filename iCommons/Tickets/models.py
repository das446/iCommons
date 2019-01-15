# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Users.models import User

# Create your models here.

class Ticket(models.Model):
    requester = models.ForeignKey(User)
    text = models.CharField(max_length=1000)
    creation_date = models.DateTimeField()
