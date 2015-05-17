# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('unique_id', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
    ]
