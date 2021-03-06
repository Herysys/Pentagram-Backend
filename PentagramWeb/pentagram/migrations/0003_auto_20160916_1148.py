# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pentagram.models


class Migration(migrations.Migration):

    dependencies = [
        ('pentagram', '0002_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pentagram.Photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=pentagram.models.photos_directory),
        ),
    ]
