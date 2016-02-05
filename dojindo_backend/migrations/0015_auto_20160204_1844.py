# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojindo_backend', '0014_auto_20160204_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='collection',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dojindo_backend.User'),
        ),
    ]