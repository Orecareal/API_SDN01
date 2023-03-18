# Generated by Django 4.1.7 on 2023-03-18 04:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_staf', '0005_alter_datamapel_created_alter_datamapel_updated_and_more'),
        ('api_guru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapelGuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 3, 18, 11, 7, 38, 391500))),
                ('updated', models.DateTimeField(default=datetime.datetime(2023, 3, 18, 11, 7, 38, 391500))),
                ('id_guru', models.ForeignKey(db_column='kd_guru', on_delete=django.db.models.deletion.CASCADE, to='api_guru.dataguru', to_field='kd_guru')),
                ('id_mapel', models.ForeignKey(db_column='kd_mapel', on_delete=django.db.models.deletion.CASCADE, to='api_staf.datamapel', to_field='kd_mapel')),
            ],
            options={
                'verbose_name_plural': 'Mapel Guru',
            },
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 11, 7, 38, 389502)),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 11, 7, 38, 390500)),
        ),
        migrations.DeleteModel(
            name='Mapel_Guru',
        ),
    ]