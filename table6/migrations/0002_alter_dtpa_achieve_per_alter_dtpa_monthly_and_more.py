# Generated by Django 4.2.4 on 2023-09-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table6', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtpa',
            name='achieve_per',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dtpa',
            name='monthly',
            field=models.CharField(default='bla', max_length=50),
        ),
        migrations.AlterField(
            model_name='dtpa',
            name='name',
            field=models.CharField(default='bla', max_length=50),
        ),
        migrations.AlterField(
            model_name='dtpa',
            name='remarks',
            field=models.CharField(default='bla', max_length=50),
        ),
    ]
