# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-03 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20190403_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
