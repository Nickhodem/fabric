# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knitting', '0006_auto_20150703_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=30)),
                ('hashname', models.CharField(unique=True, max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='tutor',
            name='surname',
            field=models.CharField(max_length=30),
        ),
    ]
