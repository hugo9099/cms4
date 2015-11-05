# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage2', '0005_auto_20151022_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='LP_version',
            field=models.ForeignKey(default=1, to='landpage2.LandPageVersion'),
        ),
    ]
