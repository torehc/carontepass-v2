# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0011_log_user_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='ts_received',
        ),
        migrations.RemoveField(
            model_name='message',
            name='ts_send',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='rol',
            field=models.CharField(default=b'Info', max_length=7, choices=[(b'Input', b'Input'), (b'Output', b'Output'), (b'Caution', b'Caution'), (b'Info', b'Info')]),
        ),
    ]
