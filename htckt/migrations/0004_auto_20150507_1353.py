# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htckt', '0003_auto_20150507_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='agg_10th_percntge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='agg_12th_percntge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='agg_BE_percntge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='passing_yr',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_date',
            field=models.CharField(max_length=50),
        ),
    ]
