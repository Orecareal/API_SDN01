# Generated by Django 4.1.7 on 2023-03-18 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0007_datakelas_delete_datamapel_alter_datastaff_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datakelas',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 578668)),
        ),
        migrations.AlterField(
            model_name='datakelas',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 578668)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 577669)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 577669)),
        ),
    ]
