# Generated by Django 4.1.7 on 2023-03-20 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_penilaian', '0013_alter_dataabsensisiswa_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataabsensisiswa',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 50, 32, 345127)),
        ),
        migrations.AlterField(
            model_name='dataabsensisiswa',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 50, 32, 345127)),
        ),
        migrations.AlterField(
            model_name='datanilaisiswa',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 50, 32, 345127)),
        ),
        migrations.AlterField(
            model_name='datanilaisiswa',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 50, 32, 345127)),
        ),
    ]
