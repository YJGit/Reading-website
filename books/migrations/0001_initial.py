# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_url', models.URLField()),
                ('score', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(blank=True, max_length=100)),
                ('translator', models.CharField(blank=True, max_length=100)),
                ('publisher_date', models.DateField()),
                ('page', models.IntegerField()),
                ('price', models.FloatField()),
                ('binding', models.CharField(blank=True, max_length=30)),
                ('Isbn', models.CharField(blank=True, max_length=100)),
                ('label', models.CharField(blank=True, max_length=100)),
                ('content_intro', models.CharField(blank=True, max_length=1000)),
                ('directory', models.CharField(blank=True, max_length=1000)),
                ('book_id', models.IntegerField()),
            ],
        ),
    ]
