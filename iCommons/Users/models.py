
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class User(AbstractUser):
    """
    main user profile model, all users will have a Profile
    """
    user_type = models.ForeignKey("UserType")
    first_name = models.CharField(max_length=100, null = True, blank=True)
    last_name = models.CharField(max_length=100, null = True, blank=True)
    email = models.CharField(max_length=100, null = True, blank=True)
    phone_regex = RegexValidator(regex=r'^\d\d\d-\d\d\d-\d\d\d\d$',
                                 message="Phone number must be entered in the format: 'XXX-XXX-XXXX'.")
    phone_number = models.CharField(
        validators=[phone_regex], null=True, blank=True, max_length=15)
    university_id = models.CharField(max_length=8, null = True, blank=True)
    major = models.CharField(max_length = 100, null = True, blank=True)
    advisor = models.ForeignKey('User',null = True, blank=True)


class UserType(models.Model):
    name = models.CharField(max_length=100)