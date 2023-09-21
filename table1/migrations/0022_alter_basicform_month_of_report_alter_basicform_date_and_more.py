# Generated by Django 4.2.5 on 2023-09-18 07:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table1', '0021_alter_basicform_month_of_report_alter_basicform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicform',
            name='Month_of_Report',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 18, 7, 10, 12, 98550, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='date',
            field=models.CharField(blank=True, default=datetime.datetime(2023, 9, 18, 7, 10, 12, 98550, tzinfo=datetime.timezone.utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='basicform', to=settings.AUTH_USER_MODEL),
        ),
    ]