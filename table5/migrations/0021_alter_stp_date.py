# Generated by Django 4.2.5 on 2023-09-18 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table5', '0020_alter_stp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stp',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 7, 0, 7, 884304, tzinfo=datetime.timezone.utc)),
        ),
    ]