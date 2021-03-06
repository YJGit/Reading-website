# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('book_title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=150)),
                ('page', models.IntegerField()),
                ('chapter', models.CharField(max_length=100)),
            ],
        ),
    ]
