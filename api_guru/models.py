from django.db import models
from api_staf.models import DataMapel
import datetime
# Create your models here.

jen_kel = [
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan')
]


jbt_guru = [
    ('Guru Mapel', 'Guru Mata Pelajaran'),
    ('Guru Kelas', 'Guru Kelas'),
    ('Guru Pendidikan Agama', 'Guru Pendidikan Agama')
]


class DataGuru(models.Model):
    kd_guru = models.CharField(max_length=13, null=False, unique=True)
    nm_guru = models.CharField(max_length=100, null=False)
    jbt_guru = models.CharField(max_length=100, choices=jbt_guru)
    jen_kel = models.CharField(max_length=12, choices=jen_kel)
    thn_aktif = models.DateField(default=datetime.datetime.now().strftime('%Y-%m-%d'))
    thn_nonaktif = models.DateField(blank=True, null=True)
    alamat = models.TextField(max_length=300, blank=True)
    no_hp = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.kd_guru} - {self.nm_guru}'

    class Meta:
         verbose_name_plural = 'Guru'


class MapelGuru(models.Model):
    id_guru = models.ForeignKey(DataGuru, to_field="kd_guru", db_column="kd_guru", on_delete=models.CASCADE)
    id_mapel = models.ForeignKey(DataMapel, to_field="kd_mapel", db_column="kd_mapel", on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())
    
    class Meta:
         verbose_name_plural = 'Mapel Guru'