# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officials', '0007_auto_20170324_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='official',
            name='answer1',
            field=models.CharField(blank=True, max_length=50, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='official',
            name='answer2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='official',
            name='answer3',
            field=models.CharField(blank=True, max_length=50, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='official',
            name='question1',
            field=models.CharField(blank=True, choices=[('question1_1', 'What is the first name of your best friend in high school?'), ('question1_2', 'What was the name of your first pet?'), ('question1_3', 'What was the first thing you learned to cook?'), ('question1_4', 'What was the first film you saw in the theater?'), ('question1_5', 'Where did you go the first time you flew on a plane?'), ('question1_6', 'What is the last name of your favorite elementary school teacher?')], max_length=50, verbose_name='Security Question 1'),
        ),
        migrations.AddField(
            model_name='official',
            name='question2',
            field=models.CharField(blank=True, choices=[('question2_1', 'What is your dream job?'), ('question2_2', 'What is your favorite children’s book?'), ('question2_3', 'What was the model of your first car?'), ('question2_4', 'What was your childhood nickname?'), ('question2_5', 'Who was your favorite film star or character in school?'), ('question2_6', 'Who was your favorite singer or band in high school?')], max_length=50, verbose_name='Security Question 2'),
        ),
        migrations.AddField(
            model_name='official',
            name='question3',
            field=models.CharField(blank=True, choices=[('question3_1', 'In what city did your parents meet?'), ('question3_2', 'What was the first name of your first boss?'), ('question3_3', 'What is the name of the street where you grew up?'), ('question3_4', 'What is the name of the first beach you visited?'), ('question3_5', 'What was the first album that you purchased?'), ('question3_6', 'What is the name of your favorite sports team?')], max_length=50, verbose_name='Security Question 3'),
        ),
    ]