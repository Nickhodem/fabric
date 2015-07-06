# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('price', models.FloatField()),
                ('place', models.CharField(max_length=500)),
                ('vacancy', models.IntegerField()),
                ('registration', models.DateField()),
                ('essence', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=30)),
                ('hashname', models.CharField(unique=True, max_length=30)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('paid', models.BooleanField(default=False)),
                ('registered_day', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=30)),
                ('actitle', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(to='knitting.Tutor', null=True),
        ),
    ]
