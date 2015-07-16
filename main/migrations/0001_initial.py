# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('post_title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('post_text', models.TextField(verbose_name='Текст сообщения')),
                ('post_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('post_likes', models.IntegerField(default=0, blank=True, verbose_name='Понравилось')),
            ],
            options={
                'db_table': 'post',
            },
            bases=(models.Model,),
        ),
    ]
