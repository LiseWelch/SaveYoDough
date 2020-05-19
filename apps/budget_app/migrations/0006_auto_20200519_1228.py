# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-19 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0005_auto_20191023_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_from',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account_to',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='card_from',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='card_to',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
