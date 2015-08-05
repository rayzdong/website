# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=datetime.datetime(2015, 8, 4, 14, 46, 28, 982817, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
