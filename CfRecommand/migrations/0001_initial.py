# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommandList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('books', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
