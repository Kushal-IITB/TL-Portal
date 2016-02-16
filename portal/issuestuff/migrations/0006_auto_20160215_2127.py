# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issuestuff', '0005_auto_20160215_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('taketime', models.DateTimeField(blank=True, null=True)),
                ('returntime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='issuinglog',
            name='stuff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issuestuff.Stuff'),
        ),
        migrations.AddField(
            model_name='issuinglog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
