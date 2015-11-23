# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0008_auto_20151111_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='ts_input',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='ts_output',
            field=models.DateTimeField(blank=True),
        ),
    ]
