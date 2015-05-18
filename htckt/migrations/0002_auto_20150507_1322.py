# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htckt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='contact',
            new_name='phone',
        ),
    ]
