# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_auto_20170405_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AttendanceResident',
            new_name='Attendance',
        ),
    ]
