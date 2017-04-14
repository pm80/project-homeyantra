# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hisab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(default='abc', max_length=50)),
                ('p_type', models.CharField(default='abc', max_length=50)),
                ('p_name', models.CharField(default='abc', max_length=50)),
                ('price', models.IntegerField(default='11')),
                ('quantity', models.IntegerField(default='11')),
                ('image', models.ImageField(upload_to='photo/')),
            ],
        ),
    ]
