# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import render
from .models import Ticket
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from Users.models import User
from iCommons import settings
from django.core.signing import BadSignature
from django.http import Http404
from django.core.signing import Signer
from django.core import mail

class TicketTestUrl(TestCase):
    def test_create_url(self):
        client = Client()
        response = client.get(reverse('tickets:create'))
        status = response.status_code
        self.assertEquals(status, 200)
        
    def test_view_all_url(self):
        client = Client()
        response = client.get(reverse('tickets:view_all'))
        status = response.status_code
        self.assertEquals(status, 200)

    def test_view_ticket_url(self):
        client=Client()
        ticket = Ticket(creation_date=datetime.now())
        ticket.requester = "tester"
        ticket.subject = "test"
        ticket.text = "test"
        ticket.save()
        signed_pk = ticket.signer.sign(ticket.pk)
        response = client.get(reverse('tickets:view_ticket',args=(signed_pk,)))
        status = response.status_code
        self.assertEquals(status, 200)

class TicketTestModels(TestCase):
    def test_absolute_url(self):
        ticket = Ticket(creation_date=datetime.now())
        ticket.save()
        t = ticket.get_absolute_url()
        self.assertIsNotNone(t)
    
    def test_view(self):
        ticket = Ticket(creation_date=datetime.now(), status= "seen", seen=True)
        ticket.save()
        t = ticket.view()
        self.assertIsNone(t)

class TicketTestViews(TestCase):
    def test_create(self):
        data = {
            'subject':'subject',

            'text':'text',

            'email':'email@mail.com',

            'time':datetime.now() 
        }
        response = self.client.post(reverse('tickets:create'), data)
        status = response.status_code
        self.assertEquals(status, 200)

    def test_send_email(self):
        mail.send_mail('Subject here', 'body', 'from@example.com', ['to@example.com'], fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
#
#   def test_view_ticket(self):
#       ticket = Ticket(creation_date=datetime.now())
#       ticket.requester = "tester"
#       ticket.subject = "test"
#       ticket.text = "test"
#       ticket.save()
#       signed_pk = ticket.signer.sign(ticket.pk)
#       with self.assertRaises(Http404):
#            signed_pk = BadSignature
