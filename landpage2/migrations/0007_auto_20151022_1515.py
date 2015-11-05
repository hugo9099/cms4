# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage2', '0006_auto_20151022_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='creation_date',
            field=models.DateTimeField(null=True, verbose_name=b'Date Created'),
        ),
    ]
