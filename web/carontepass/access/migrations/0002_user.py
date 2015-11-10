# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=120)),
                ('rol', models.CharField(default=b'USER', max_length=4, choices=[(b'USER', b'User'), (b'ADMI', b'Administrator')])),
                ('phone', models.CharField(max_length=18)),
                ('address', models.CharField(max_length=220)),
                ('email', models.CharField(max_length=180)),
                ('group', models.ForeignKey(to='access.Group')),
            ],
        ),
    ]
