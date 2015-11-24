# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0010_auto_20151116_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='user_in',
            field=models.BooleanField(default=False),
        ),
    ]
