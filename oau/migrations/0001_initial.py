# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, blank='')),
                ('sex', models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male'), ('N', "I'd rather not disclose")])),
                ('level', models.CharField(max_length=1, choices=[('1', 'Part 1'), ('2', 'Part 2'), ('3', 'Part 3'), ('4', 'Part 4'), ('5', 'Part 5')])),
                ('knowledge', models.CharField(max_length=3, choices=[('BEG', 'I have never used it before'), ('AMA', 'I have used it once or twice'), ('BUI', 'I have built some stuff with Python')])),
                ('display_image', models.BooleanField(default=True)),
                ('message', models.TextField(default='', max_length=500)),
                ('bio', models.TextField(default='', max_length=100)),
                ('interest', models.CharField(max_length=3, choices=[('PYT', 'Pure Python Scripting'), ('WEB', 'Web Programming'), ('DTS', 'Data Science'), ('APP', 'App Development(Mostly Kivy and other GUIs libraries)'), ('NET', 'Networking'), ('NDI', 'I do not know for now.')])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to='oau.Member')),
            ],
        ),
    ]
