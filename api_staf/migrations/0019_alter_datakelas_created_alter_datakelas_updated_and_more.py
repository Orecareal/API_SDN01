# Generated by Django 4.1.7 on 2023-03-20 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0018_alter_datakelas_created_alter_datakelas_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datakelas',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 7, 46, 38, 398474)),
        ),
        migrations.AlterField(
            model_name='datakelas',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 7, 46, 38, 398474)),
        ),
        migrations.AlterField(
            model_name='datakeuangan',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 7, 46, 38, 398474)),
        ),
        migrations.AlterField(
            model_name='datakeuangan',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 7, 46, 38, 398474)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 7, 46, 38, 398474)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 7, 46, 38, 398474)),
        ),
    ]
