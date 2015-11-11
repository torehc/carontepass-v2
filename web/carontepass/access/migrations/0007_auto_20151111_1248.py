# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0006_auto_20151110_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='ts_received',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='ts_send',
            field=models.DateTimeField(),
        ),
    ]
