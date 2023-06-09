# Generated by Django 4.1.7 on 2023-03-18 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_guru', '0004_datamapel_alter_dataguru_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 576670)),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 576670)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 576670)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 576670)),
        ),
        migrations.AlterField(
            model_name='mapelguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 577669)),
        ),
        migrations.AlterField(
            model_name='mapelguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 3, 44, 577669)),
        ),
    ]
