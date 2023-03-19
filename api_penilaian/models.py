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

test = [
    ('Latihan', 'Latihan'),
    ('Pekerjaan Rumah', 'PR'),
    ('Ulangan Semester I', 'Ulangan Semester I'),
    ('Ulangan Semester II', 'Ulangan Semester II'),
    ('Ujian Semester I', 'Ujian Semester I'),
    ('Ujian Semester II', 'Ujian Semester II'),
]

class DataAbsensiSiswa(models.Model):
    kd_kelas = models.ForeignKey(DataKelas, on_delete=models.CASCADE, verbose_name="Pilih Kelas")
    kd_mapel = models.ForeignKey(MapelGuru, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=30, choices=att)
    catatan = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.kd_kelas}  {self.kd_mapel}'

    class Meta:
         verbose_name_plural = 'Absensi Siswa'


class DataNilaiSiswa(models.Model):
    id_abs = models.ForeignKey(DataAbsensiSiswa, on_delete=models.CASCADE, verbose_name="Absensi siswa")
    test_type = models.CharField(max_length=30, choices=test)
    nilai = models.FloatField(default=0.00)
    catatan = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
            return f'{self.test_type} / {self.nilai}'


    class Meta:
         verbose_name_plural = 'Penilaian Siswa'