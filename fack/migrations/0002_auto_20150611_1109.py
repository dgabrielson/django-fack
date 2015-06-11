# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created on'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='updated on'),
            preserve_default=True,
        ),
    ]
