# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id_ingreso', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
