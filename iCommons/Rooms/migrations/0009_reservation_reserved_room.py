# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-15 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0008_auto_20190410_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reserved_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Rooms.Room'),
        ),
    ]
