# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='laber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher_date',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='score',
            field=models.FloatField(),
        ),
    ]