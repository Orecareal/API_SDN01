# Generated by Django 4.1.7 on 2023-03-20 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_akutansi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapembayaran',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 0, 5, 345603)),
        ),
        migrations.AlterField(
            model_name='datapembayaran',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 0, 5, 345603)),
        ),
    ]
