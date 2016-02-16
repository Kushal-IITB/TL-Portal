# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuestuff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='department',
        ),
        migrations.AddField(
            model_name='member',
            name='contact',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='discipline',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='graduation_year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='hostel',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='join_year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='roll',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='room',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Others')], max_length=10, null=True),
        ),
    ]
