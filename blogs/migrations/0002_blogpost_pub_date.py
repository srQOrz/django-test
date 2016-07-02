# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 10:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 2, 10, 6, 39, 632137, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
