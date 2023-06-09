# Generated by Django 4.1.7 on 2023-03-19 08:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_staf', '0013_alter_datakelas_created_alter_datakelas_updated_and_more'),
        ('api_guru', '0010_alter_dataguru_created_alter_dataguru_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataAbsensiSiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.CharField(choices=[('H', 'Hadir'), ('S', 'Sakit'), ('I', 'Izin'), ('A', 'Tidak Hadir'), ('-', 'Tanpa Keterangan')], max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 19, 17, 878698))),
                ('updated', models.DateTimeField(default=datetime.datetime(2023, 3, 19, 15, 19, 17, 878698))),
                ('kd_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_staf.datakelas', verbose_name='Pilih Kelas')),
                ('kd_mapel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_guru.mapelguru')),
            ],
            options={
                'verbose_name_plural': 'Absensi Siswa',
            },
        ),
    ]
