# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Users.models import User

# Create your models here.


class Ticket(models.Model):
    requester = models.ForeignKey(User)
    subject = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=1000, null=True)
    creation_date = models.DateTimeField()
    status = models.CharField(max_length=100, null=True)
    seen = models.BooleanField(default=False)
