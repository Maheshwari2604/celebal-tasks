# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-29 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbo', '0004_auto_20190829_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='task_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='dbo.task'),
            preserve_default=False,
        ),
    ]
