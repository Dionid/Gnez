# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gnAuth', '0002_auto_20170623_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='gnuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
