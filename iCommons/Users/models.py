# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import helpers

# Create your models here.


class UserProfile(models.Model):
    """
    main user profile model, all users will have a Profile
    """
    user = models.OneToOneField(User)
    user_type = models.CharField(helpers.Roles)
