# Generated by Django 4.1.7 on 2023-03-19 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0015_alter_datakelas_created_alter_datakelas_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datakelas',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 34, 24, 933215)),
        ),
        migrations.AlterField(
            model_name='datakelas',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 34, 24, 933215)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 34, 24, 933215)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 34, 24, 933215)),
        ),
    ]