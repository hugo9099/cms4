# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage2', '0004_auto_20151022_1432'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LP_Version',
            new_name='LandPageVersion',
        ),
    ]
