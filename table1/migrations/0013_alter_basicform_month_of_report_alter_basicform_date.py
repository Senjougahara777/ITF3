# Generated by Django 4.2.4 on 2023-09-14 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table1', '0012_alter_basicform_month_of_report_alter_basicform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicform',
            name='Month_of_Report',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 14, 11, 13, 13, 384533, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='date',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 14, 11, 13, 13, 384533, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]