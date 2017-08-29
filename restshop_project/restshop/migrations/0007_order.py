# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restshop', '0006_auto_20170828_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('unit_set', models.ManyToManyField(to='restshop.Unit')),
            ],
        ),
    ]