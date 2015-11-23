# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0009_auto_20151116_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='ts_input',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='log',
            name='ts_output',
            field=models.DateTimeField(),
        ),
    ]
