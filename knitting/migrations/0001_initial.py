# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('tutors', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('price', models.FloatField()),
                ('place', models.CharField(max_length=500)),
                ('vacancy', models.IntegerField()),
                ('registration', models.DateField()),
                ('essence', models.TextField()),
            ],
        ),
    ]
