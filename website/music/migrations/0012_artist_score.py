# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-26 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_remove_artist_picture_of_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='score',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
