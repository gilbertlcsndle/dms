# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='name',
            new_name='file',
        ),
    ]
