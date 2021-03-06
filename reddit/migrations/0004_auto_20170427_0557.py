# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 05:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0003_post_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='vote',
        ),
        migrations.AddField(
            model_name='vote',
            name='on_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='reddit.Post'),
        ),
        migrations.AddField(
            model_name='vote',
            name='voted_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
