# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 14:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residents', '0004_auto_20170311_2203'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('kap', 'Punong Barangay'), ('kg', 'Kagawad'), ('sec', 'Secretary'), ('tr', 'Treasurer')], default='', max_length=50)),
                ('residents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
