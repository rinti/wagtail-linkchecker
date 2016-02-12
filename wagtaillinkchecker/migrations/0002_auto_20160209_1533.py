# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaillinkchecker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitepreferences',
            name='automated_scanning',
            field=models.BooleanField(default=False, help_text='Conduct automated sitewide scans for broken links, and send emails if a problem is found.'),
        ),
        migrations.AlterField(
            model_name='sitepreferences',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site'),
        ),
    ]
