# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0007_auto_20151111_1248'),
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
        migrations.AlterField(
            model_name='payment',
            name='f_payment',
            field=models.DateTimeField(),
        ),
    ]
