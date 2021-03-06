# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 18:24
from __future__ import unicode_literals

from django.db import migrations, models


def update_name_from_date(apps, schema_editor):
    DataSet = apps.get_model('api', 'DataSet')
    for ds in DataSet.objects.all():
        ds.name = ds.date.isoformat()
        ds.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_on_delete_cascade_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='name',
            field=models.CharField(default='update-me', max_length=50),
            preserve_default=False,
        ),
        migrations.RunPython(update_name_from_date, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
