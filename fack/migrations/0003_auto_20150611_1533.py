# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fack', '0002_auto_20150611_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionscore',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='IP address', blank=True),
        ),
    ]
