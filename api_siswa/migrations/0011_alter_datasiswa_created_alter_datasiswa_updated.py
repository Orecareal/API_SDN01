# Generated by Django 4.1.7 on 2023-03-19 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_siswa', '0010_alter_datasiswa_created_alter_datasiswa_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 34, 24, 928225)),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 34, 24, 928225)),
        ),
    ]
