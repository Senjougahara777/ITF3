# Generated by Django 4.2.4 on 2023-09-14 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table5', '0013_alter_stp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stp',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 11, 57, 6, 429533, tzinfo=datetime.timezone.utc)),
        ),
    ]
