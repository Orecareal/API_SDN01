# Generated by Django 4.1.7 on 2023-03-18 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0003_alter_datamapel_created_alter_datamapel_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamapel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 10, 52, 29, 987837)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='kd_mapel',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 10, 52, 29, 987837)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 10, 52, 29, 987837)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='kd_staf',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 10, 52, 29, 987837)),
        ),
    ]