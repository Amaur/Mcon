# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('inicial', models.DateTimeField(auto_now=True)),
                ('fim', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-fim'],
                'verbose_name': 'Dinar',
                'verbose_name_plural': 'Dinares',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('nombre', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(max_digits=10, decimal_places=4)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('isException', models.BooleanField(default=False)),
                ('dinar', models.ForeignKey(to='con.Dinar')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
