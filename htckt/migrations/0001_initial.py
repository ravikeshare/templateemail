# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
                ('contact', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")])),
                ('reg_date', models.DateField(default=django.utils.timezone.now)),
                ('institute_name', models.CharField(max_length=200)),
                ('passing_yr', models.CharField(max_length=4, choices=[('1', '2013'), ('2', '2014'), ('3', '2015')])),
                ('agg_10th_percntge', models.DecimalField(default=Decimal('0.00'), max_digits=5, decimal_places=2)),
                ('agg_12th_percntge', models.DecimalField(default=Decimal('0.00'), max_digits=5, decimal_places=2)),
                ('agg_BE_percntge', models.DecimalField(default=Decimal('0.00'), max_digits=5, decimal_places=2)),
                ('branch', models.CharField(max_length=50)),
                ('tpo_email', models.EmailField(max_length=80)),
            ],
        ),
    ]
