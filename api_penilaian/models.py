from django.db import models
from api_staf.models import DataKelas
from api_guru.models import MapelGuru
import datetime

# Create your models here.

att = [
    ('H', 'Hadir'),
    ('S', 'Sakit'),
    ('I', 'Izin'),
    ('A', 'Tidak Hadir'),
    ('-', 'Tanpa Keterangan'),
]

class DataAbsensiSiswa(models.Model):
    kd_kelas = models.ForeignKey(DataKelas, on_delete=models.CASCADE, verbose_name="Pilih Kelas")
    kd_mapel = models.ForeignKey(MapelGuru, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=30, choices=att)
    catatatn = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.kd_kelas}  {self.kd_mapel}'

    class Meta:
         verbose_name_plural = 'Absensi Siswa'
