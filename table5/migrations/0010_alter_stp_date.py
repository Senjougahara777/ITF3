# Generated by Django 4.2.4 on 2023-09-13 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table5', '0009_alter_stp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stp',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 13, 11, 21, 59, 484308, tzinfo=datetime.timezone.utc)),
        ),
    ]
