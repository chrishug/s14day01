# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Group'),
        ),
    ]