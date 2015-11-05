# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage2', '0002_auto_20151022_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='version',
            new_name='LP_version',
        ),
    ]
