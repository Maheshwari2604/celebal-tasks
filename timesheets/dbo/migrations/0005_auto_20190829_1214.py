# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-29 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbo', '0004_auto_20190829_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='project',
            field=models.IntegerField(),
        ),
    ]
