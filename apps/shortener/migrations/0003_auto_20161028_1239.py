# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161028_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(db_index=True, max_length=128),
        ),
    ]