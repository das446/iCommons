# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, UserType

from django import forms
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	exclude = ('password',)

admin.site.register(User, UserAdmin)
admin.site.register(UserType)


