# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150617_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='post_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='post_likes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='post_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
    ]
