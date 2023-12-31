# Generated by Django 4.2.5 on 2023-09-18 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table1', '0018_alter_basicform_month_of_report_alter_basicform_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicform',
            name='rejected2',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='Month_of_Report',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 18, 5, 1, 29, 900162, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='date',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 18, 5, 1, 29, 900162, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]
