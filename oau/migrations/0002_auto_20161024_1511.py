# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oau', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('event_title', models.CharField(max_length=300, default='')),
                ('start_date', models.CharField(max_length=2, default='')),
                ('end_date', models.CharField(max_length=2, blank=True, default='')),
                ('details', models.TextField(blank=True, default='')),
                ('event', models.CharField(choices=[('PYT', 'Python Club Event'), ('GEN', 'General Event')], max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='members/image/mathhew.png', upload_to='members/image'),
        ),
        migrations.AlterField(
            model_name='member',
            name='display_image',
            field=models.BooleanField(default=False),
        ),
    ]
