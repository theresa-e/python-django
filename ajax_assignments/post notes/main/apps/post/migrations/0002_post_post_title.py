# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-02 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
