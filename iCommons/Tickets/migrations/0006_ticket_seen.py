# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-13 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0005_auto_20190427_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
