# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='children',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='resident',
            name='iodized_salt',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='resident',
            name='lactating',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='resident',
            name='sangkap_pinoy_seal_product',
            field=models.BooleanField(),
        ),
    ]
