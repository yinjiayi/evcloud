# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbgpu',
            name='vm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compute.Vm'),
        ),
    ]