# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160929_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
