# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-02 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_lesson_learn_times'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseresource',
            name='download',
        ),
    ]
