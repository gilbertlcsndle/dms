# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20170404_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceofficial',
            name='event',
        ),
        migrations.RemoveField(
            model_name='attendanceofficial',
            name='official',
        ),
        migrations.AlterField(
            model_name='attendanceresident',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residents.Resident', verbose_name='id no'),
        ),
        migrations.DeleteModel(
            name='AttendanceOfficial',
        ),
    ]
