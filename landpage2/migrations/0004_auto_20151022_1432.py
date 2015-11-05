# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage2', '0003_auto_20151022_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='LP_Version',
            fields=[
                ('lpver', models.IntegerField(serialize=False, verbose_name=b'Landing Page Version', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('look', models.ImageField(upload_to=b'')),
                ('description', models.TextField()),
                ('creation_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='leadtype',
            options={'ordering': ['type']},
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='phone_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='leadtype',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='leadtype',
            name='specs',
            field=models.URLField(null=True),
        ),
    ]
