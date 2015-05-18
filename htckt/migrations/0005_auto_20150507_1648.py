# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htckt', '0004_auto_20150507_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='position',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
