# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 11:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_auto_20180613_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thump',
        ),
        migrations.AddField(
            model_name='article',
            name='auther',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
