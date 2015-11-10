# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=512)),
                ('ts_send', models.DateTimeField(auto_now=True)),
                ('ts_received', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to='access.User')),
            ],
        ),
    ]
