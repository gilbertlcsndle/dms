# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start', models.CharField(max_length=50)),
                ('end', models.CharField(max_length=50)),
            ],
        ),
    ]
