# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20180613_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default=b'default.jpeg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='article',
            name='thump',
            field=models.ImageField(blank=True, default=b'default.png', upload_to=b''),
        ),
    ]
