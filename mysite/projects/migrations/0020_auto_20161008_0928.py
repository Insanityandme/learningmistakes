# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_category_hide'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='contenttype',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='box_size',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='thumbnail_width',
        ),
    ]
