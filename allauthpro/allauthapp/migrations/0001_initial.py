# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-08 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=25)),
                ('emp_id', models.CharField(max_length=5)),
                ('email_id', models.CharField(max_length=30)),
                ('gen', models.CharField(max_length=1)),
                ('dept', models.CharField(max_length=15)),
                ('exp', models.CharField(max_length=16)),
                ('skills', models.CharField(max_length=50)),
                ('fdbk', models.CharField(max_length=500)),
            ],
        ),
    ]