# Generated by Django 4.2.5 on 2023-09-18 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table1', '0020_alter_basicform_month_of_report_alter_basicform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicform',
            name='Month_of_Report',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 18, 7, 0, 7, 871292, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='date',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 18, 7, 0, 7, 871292, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]
