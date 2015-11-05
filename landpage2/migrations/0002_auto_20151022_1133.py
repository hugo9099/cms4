# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadtype',
            name='specs',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='leadtype',
            name='type',
            field=models.IntegerField(verbose_name=b'Booberdoo Lead Type ID'),
        ),
    ]
