# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-31 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0003_device_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Charger', 'Charger'), ('HDMI', 'HDMI')], max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[('Reserved', 'Reserved'), ('Loaned Out', 'Loaned Out'), ('Available', 'Available')], max_length=100),
        ),
    ]