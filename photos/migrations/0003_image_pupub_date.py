# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pupub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
