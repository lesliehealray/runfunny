# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='poster',
            name='posts',
            field=models.ManyToManyField(to='run.VideoPost'),
        ),
    ]
