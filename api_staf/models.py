from django.db import models
from api_siswa.models import DataSiswa
from api_guru.models import DataGuru
import datetime

# Create your models here.


jen_kel = [
    ('L', 'Laki-laki'),
    ('P', 'Perempuan')
]

kelas = [
    ('1A', '1A'),
    ('2A', '2B'),
    ('3A', '3B'),
    ('4A', '4B'),
    ('5A', '5B'),
    ('6A', '6B'),
]
class DataStaff(models.Model):
    kd_staf = models.CharField(max_length=13, null=False, unique=True)
    nm_staff = models.CharField(max_length=100, null=False)
    jen_kel = models.CharField(max_length=12, choices=jen_kel)
    thn_aktif = models.DateField(default=datetime.datetime.now().strftime('%Y-%m-%d'))
    thn_nonaktif = models.DateField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
         verbose_name_plural = 'Staff'

         

class DataKelas(models.Model):
    kd_kelas = models.CharField(max_length=13, choices=kelas)
    id_guru = models.ForeignKey(DataGuru, to_field="kd_guru", blank=True, null=True, on_delete=models.CASCADE)
    id_siswa = models.ForeignKey(DataSiswa, to_field="nis_siswa", blank=True, null=True, on_delete=models.CASCADE)
    lama_jam = models.CharField(max_length=10)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return f'{self.kd_kelas},{self.kd_guru}'
        
    class Meta:
         verbose_name_plural = 'Kelas'