# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idm_card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='max_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='printed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
