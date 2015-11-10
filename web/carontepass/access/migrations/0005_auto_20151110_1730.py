# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_device_log_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='url',
            field=models.CharField(max_length=160, verbose_name=b'Url Web'),
        ),
    ]
