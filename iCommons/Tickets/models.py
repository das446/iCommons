# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Users.models import User

from django.core.signing import Signer

from django.urls import reverse

# Create your models here.


class Ticket(models.Model):

    signer = Signer(sep='/', salt='ticket.Ticket')

    requester = models.ForeignKey(User)
    subject = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=1000, null=True)
    creation_date = models.DateTimeField()
    status = models.CharField(max_length=100, null=True)
    #seen = models.BooleanField(default=False)

    def get_absolute_url(self):
        signed_pk = self.signer.sign(self.pk)
        return reverse('ticket-view', kwargs={'signed_pk': signed_pk})

    def view(self):
        self.status = "seen"
        self.seen = True