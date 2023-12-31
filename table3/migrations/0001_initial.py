# Generated by Django 4.2.4 on 2023-09-03 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TNA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField()),
                ('tnac', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tna', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
