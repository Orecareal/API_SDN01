# Generated by Django 4.1.7 on 2023-03-20 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_siswa', '0017_alter_datasiswa_created_alter_datasiswa_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 38, 13, 377811)),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 38, 13, 377811)),
        ),
    ]
