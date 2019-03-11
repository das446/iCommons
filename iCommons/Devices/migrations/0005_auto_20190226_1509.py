# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-26 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devices', '0004_auto_20190131_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoanStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.DeviceType'),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.DeviceStatus'),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Devices.LoanStatus'),
        ),
    ]