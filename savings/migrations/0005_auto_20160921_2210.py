# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-21 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0004_auto_20160918_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileuser',
            old_name='purchasing_power',
            new_name='consumption',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='control_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='income',
            field=models.IntegerField(choices=[(1, 'very low'), (2, 'low'), (3, 'medium'), (4, 'high'), (5, 'very high')], default=0),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='saving_capacity',
            field=models.IntegerField(choices=[(1, 'very low'), (2, 'low'), (3, 'medium'), (4, 'high'), (5, 'very high')], default=0),
        ),
    ]