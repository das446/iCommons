# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.shortcuts import render
from .models import Ticket
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from Users.models import User
from iCommons import settings
from django.core.signing import BadSignature
from django.http import Http404

# Create your tests here.
class TicketTestCase(TestCase):
    # Test that email sends
    def test_send_email(self):

        self.assertTrue(send_mail(self))
    