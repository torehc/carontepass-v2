# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default=b'nfc', max_length=3, choices=[(b'nfc', b'NFC'), (b'mac', b'MAC')])),
                ('code', models.CharField(max_length=64)),
                ('user', models.ForeignKey(to='access.User')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ts_input', models.DateTimeField(auto_now=True)),
                ('ts_output', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to='access.User')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('f_payment', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(max_digits=4, decimal_places=2)),
                ('user', models.ForeignKey(to='access.User')),
            ],
        ),
    ]
