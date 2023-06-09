# Generated by Django 4.1.7 on 2023-03-18 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis_siswa', models.CharField(max_length=13, unique=True)),
                ('nm_siswa', models.CharField(max_length=100)),
                ('jen_kel', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=12)),
                ('thn_masuk', models.DateField(default='2023-03-18')),
                ('thn_lulus', models.DateField(blank=True, null=True)),
                ('alamat', models.TextField(blank=True, max_length=300)),
                ('no_telp', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 3, 18, 15, 24, 57, 261355))),
                ('updated', models.DateTimeField(default=datetime.datetime(2023, 3, 18, 15, 24, 57, 261355))),
            ],
            options={
                'verbose_name_plural': 'Guru',
            },
        ),
    ]
