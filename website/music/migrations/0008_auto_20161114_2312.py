# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-14 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20161114_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='picture_of_artist',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
