# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('default_src', models.CharField(max_length=45, null=True, blank=True)),
                ('default_affref', models.CharField(max_length=45, null=True, blank=True)),
                ('phone_number', models.IntegerField(default=1, blank=True)),
                ('index_phone_header', models.BooleanField(default=1)),
                ('index_phone_footer', models.BooleanField(default=1)),
                ('form_phone_header', models.BooleanField(default=1)),
                ('form_phone_footer', models.BooleanField(default=1)),
                ('thankyou_phone_header', models.BooleanField(default=1)),
                ('thankyou_phone_footer', models.BooleanField(default=1)),
                ('self_emp', models.BooleanField(default=1)),
                ('insured', models.BooleanField(default=1)),
                ('spouse', models.BooleanField(default=1)),
                ('no_of_children', models.BooleanField(default=1)),
                ('est_income', models.BooleanField(default=1)),
                ('affordable', models.BooleanField(default=1)),
                ('hospitalized', models.BooleanField(default=1)),
                ('physician', models.BooleanField(default=1)),
                ('prescription', models.BooleanField(default=1)),
                ('previously_denied', models.BooleanField(default=1)),
                ('ss_disabled', models.BooleanField(default=1)),
                ('pregnant', models.BooleanField(default=1)),
                ('health', models.BooleanField(default=1)),
                ('household_size', models.BooleanField(default=1)),
                ('expected_income', models.BooleanField(default=1)),
                ('click_agree_terms_cond', models.BooleanField(default=1)),
                ('affil_contact', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='LeadType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='lead_type',
            field=models.ForeignKey(to='landpage2.LeadType'),
        ),
    ]
