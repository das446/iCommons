# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import render
from .models import User
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from Users.models import User
from iCommons import settings
from django.core.signing import BadSignature
from django.http import Http404
from django.core.signing import Signer
from django.core import mail
from django.contrib.auth import login, authenticate
# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', email='mail@mail.com', password='password')
    def test_create_url(self):
        client = Client()
        response = client.get(reverse('users:account'))
        status = response.status_code
        self.assertEquals(status, 200)

    def test_update_account(self):
        client = Client()
        response = client.post(reverse('users:account'))
        status = response.status_code
        self.assertEquals(status, 200)

    def test_login(self):
        client = Client()
        login = self.client.login(username='username', password='password')
        self.assertIsNotNone(login)

    def test_login_get(self):
        client = Client()
        response = client.get(reverse('users:login'))
        status = response.status_code
        self.assertEquals(status, 200)