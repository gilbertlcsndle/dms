# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officials', '0009_auto_20170407_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='official',
            name='question1',
            field=models.CharField(choices=[('What is the first name of your best friend in high school?', 'What is the first name of your best friend in high school?'), ('What was the name of your first pet?', 'What was the name of your first pet?'), ('What was the first thing you learned to cook?', 'What was the first thing you learned to cook?'), ('What was the first film you saw in the theater?', 'What was the first film you saw in the theater?'), ('Where did you go the first time you flew on a plane?', 'Where did you go the first time you flew on a plane?'), ('What is the last name of your favorite elementary school teacher?', 'What is the last name of your favorite elementary school teacher?')], max_length=50, verbose_name='Security Question 1'),
        ),
    ]
