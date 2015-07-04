# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knitting', '0003_auto_20150703_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tutors',
            field=models.ForeignKey(to='knitting.Tutor', to_field=b'surname'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='surname',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
