# Generated by Django 4.1.7 on 2023-03-18 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_guru', '0007_alter_dataguru_created_alter_dataguru_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 5, 59, 48, 913868)),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='thn_aktif',
            field=models.DateField(default='2023-03-19'),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 5, 59, 48, 913868)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 5, 59, 48, 914869)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 5, 59, 48, 914869)),
        ),
        migrations.AlterField(
            model_name='mapelguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 5, 59, 48, 915868)),
        ),
        migrations.AlterField(
            model_name='mapelguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 5, 59, 48, 915868)),
        ),
    ]