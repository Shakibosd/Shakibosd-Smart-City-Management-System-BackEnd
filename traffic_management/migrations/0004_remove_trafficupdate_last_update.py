# Generated by Django 5.1.2 on 2024-10-20 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_management', '0003_alter_trafficupdate_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficupdate',
            name='last_update',
        ),
    ]