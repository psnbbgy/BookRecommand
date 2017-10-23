# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CfRecommand', '0003_auto_20171018_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookids',
            name='book_id',
            field=models.IntegerField(default=0),
        ),
    ]
