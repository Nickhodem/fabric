# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knitting', '0002_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tutors',
            field=models.ForeignKey(to='knitting.Tutor'),
        ),
    ]
