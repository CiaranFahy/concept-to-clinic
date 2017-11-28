# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 19:24
from __future__ import unicode_literals

import backend.cases.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_radiology_reporting_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='review_result',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'MARKED'), (2, 'DISMISSED')], default=backend.cases.enums.CandidateReviewResult(0)),
        ),
    ]