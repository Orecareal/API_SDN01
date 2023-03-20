# Generated by Django 4.1.7 on 2023-03-20 01:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0021_alter_datakelas_created_alter_datakelas_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datakelas',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 848294)),
        ),
        migrations.AlterField(
            model_name='datakelas',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 848294)),
        ),
        migrations.AlterField(
            model_name='datakeuangan',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 849293)),
        ),
        migrations.AlterField(
            model_name='datakeuangan',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 849293)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 848294)),
        ),
        migrations.AlterField(
            model_name='datastaff',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 848294)),
        ),
        migrations.CreateModel(
            name='DataBerita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('isi', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 849293))),
                ('updated', models.DateTimeField(default=datetime.datetime(2023, 3, 20, 8, 24, 13, 849293))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_staf.datastaff', to_field='kd_staf')),
            ],
            options={
                'verbose_name_plural': 'Berita & Acara',
            },
        ),
    ]
