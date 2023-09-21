# Generated by Django 4.2.5 on 2023-09-18 07:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table5', '0022_alter_stp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stp',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 7, 15, 5, 111929, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='stp',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='stp', to=settings.AUTH_USER_MODEL),
        ),
    ]
