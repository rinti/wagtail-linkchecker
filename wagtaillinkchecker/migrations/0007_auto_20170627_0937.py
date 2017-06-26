# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaillinkchecker', '0006_scanlink_invalid'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanlink',
            name='page_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scanlink',
            name='page_slug',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='scanlink',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page'),
        ),
    ]
