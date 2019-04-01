
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.forms import ResetPasswordForm, EmailAwarePasswordResetTokenGenerator
from allauth.utils import build_absolute_uri
from allauth.account.utils import user_pk_to_url_str
from django.core.validators import RegexValidator
from django.core.mail import send_mail, EmailMultiAlternatives
from iCommons import settings
from django.urls import reverse
from django.contrib.sites.models import Site
#from .helpers import UserCreationForm

# Create your models here.

class User(AbstractUser):
    """
    main user profile model, all users will have a Profile
    """
    user_type = models.ForeignKey("UserType", default = 2)
    first_name = models.CharField(max_length=100, null = True, blank=True)
    last_name = models.CharField(max_length=100, null = True, blank=True)
    email = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\d\d\d-\d\d\d-\d\d\d\d$',
                                 message="Phone number must be entered in the format: 'XXX-XXX-XXXX'.")
    phone_number = models.CharField(
        validators=[phone_regex], null=True, blank=True, max_length=15)
    university_id = models.CharField(max_length=8, null = True, blank=True)
    major = models.CharField(max_length = 100, null = True, blank=True)
    advisor = models.ForeignKey('User',null = True, blank=True)

    #modified from allauth.ResetPasswordForm
    def send_password_reset_email(self):
        current_site = "icommons.drexel.edu"
        to_email = self.email
        token_generator = EmailAwarePasswordResetTokenGenerator()

        user = self
        temp_key = token_generator.make_token(user)

        # save it to the password reset model
        # password_reset = PasswordReset(user=user, temp_key=temp_key)
        # password_reset.save()

        # send the password reset email
        path = reverse("account_reset_password_from_key",
                    kwargs=dict(uidb36=user_pk_to_url_str(user),
                                key=temp_key))
        url = self.current_site_url() + path

        subject = "An account has been created for you"
        text = "A Student Worker account has been created for you. Please click here to set your password " + url

        send_mail(subject, text, "ihelp.accounts@drexel.edu", [to_email], fail_silently=False) 

    def save(self, *args, **kwargs):
        super(User,self).save(*args, **kwargs)
        if self.password is None or self.password=="":
            self.send_password_reset_email()
            print("sent password email")
        else:
            print(self.password)

    def current_site_url(self):
        current_site = Site.objects.get_current()
        protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
        port     = getattr(settings, 'MY_SITE_PORT', '')
        url = '%s://%s' % (protocol, current_site.domain)
        if port:
            url += ':%s' % port

        url = "http://127.0.0.1:8000"

        return settings.url



class UserType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

