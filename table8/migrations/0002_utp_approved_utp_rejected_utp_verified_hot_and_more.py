# Generated by Django 4.2.4 on 2023-09-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table8', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utp',
            name='approved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='utp',
            name='rejected',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='utp',
            name='verified_hot',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='utp',
            name='verified_manager',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
