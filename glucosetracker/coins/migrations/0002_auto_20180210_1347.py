# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin',
            options={'verbose_name_plural': 'Coins'},
        ),
        migrations.AlterModelOptions(
            name='cryptocurrency',
            options={'verbose_name_plural': 'Cryptocurrencies'},
        ),
    ]
