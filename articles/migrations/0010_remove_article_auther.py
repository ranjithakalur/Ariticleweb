# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20180613_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='auther',
        ),
    ]