# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-29 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbo', '0002_auto_20190829_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='task_type',
        ),
    ]
