# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnAuth', '0003_gnuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='gnuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
