# Generated by Django 5.1.2 on 2024-10-31 14:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analytics', '0003_remove_analyticsdata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticsdata',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
