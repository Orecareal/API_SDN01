# Generated by Django 4.1.7 on 2023-03-18 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datamapel',
            options={'verbose_name_plural': 'Mapel'},
        ),
        migrations.AlterModelOptions(
            name='datastaff',
            options={'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 8, 5, 1, 556802)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 8, 5, 1, 556802)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 8, 5, 1, 555802)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='thn_nonaktif',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 8, 5, 1, 555802)),
        ),
    ]
