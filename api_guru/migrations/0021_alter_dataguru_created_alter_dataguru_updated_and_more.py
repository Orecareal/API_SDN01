# Generated by Django 4.1.7 on 2023-03-20 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_guru', '0020_alter_dataguru_created_alter_dataguru_jbt_guru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 640801)),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 640801)),
        ),
        migrations.AlterField(
            model_name='datakonseling',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 642799)),
        ),
        migrations.AlterField(
            model_name='datakonseling',
            name='status',
            field=models.CharField(choices=[('Berjalan', 'Berjalan'), ('Selesai', 'Selesai')], max_length=30),
        ),
        migrations.AlterField(
            model_name='datakonseling',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 642799)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 641801)),
        ),
        migrations.AlterField(
            model_name='datamapel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 641801)),
        ),
        migrations.AlterField(
            model_name='mapelguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 641801)),
        ),
        migrations.AlterField(
            model_name='mapelguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 18, 40, 24, 641801)),
        ),
    ]