# Generated by Django 4.2.4 on 2023-09-14 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table1', '0015_rename_verified_cpd_basicform_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicform',
            name='Month_of_Report',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 14, 12, 34, 40, 534908, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='date',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 14, 12, 34, 40, 534908, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]