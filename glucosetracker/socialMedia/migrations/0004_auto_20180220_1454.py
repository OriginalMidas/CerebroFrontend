# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 20:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialMedia', '0003_auto_20180212_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'get_latest_by': 'createdAt'},
        ),
        migrations.AlterModelOptions(
            name='redditpost',
            options={'get_latest_by': 'createdAt'},
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'get_latest_by': 'createdAt'},
        ),
    ]
