# Generated by Django 4.2.4 on 2023-09-14 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table1', '0011_basicform_rejected_basicform_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicform',
            name='Month_of_Report',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 14, 10, 7, 55, 841814, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='date',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 14, 10, 7, 55, 841814, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]
