# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knitting', '0004_auto_20150703_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tutors',
            field=models.ForeignKey(related_name='+', to='knitting.Tutor'),
        ),
    ]
