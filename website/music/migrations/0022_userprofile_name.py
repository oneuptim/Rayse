# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-18 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]