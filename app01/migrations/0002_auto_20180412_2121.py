# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('like_article', 'user')]),
        ),
    ]
