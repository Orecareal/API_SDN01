from django.db import models
import datetime

# Create your models here.
jen_kel = [
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan')
]


class DataSiswa(models.Model):
    nis_siswa = models.CharField(max_length=13, unique=True)
    nm_siswa = models.CharField(max_length=100, null=False)
    jen_kel = models.CharField(max_length=12, choices=jen_kel)
    thn_masuk = models.DateField(default=datetime.datetime.now().strftime('%Y-%m-%d'))
    thn_lulus = models.DateField(blank=True, null=True)
    alamat = models.TextField(max_length=300, blank=True)
    no_telp = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.nis_siswa} - {self.nm_siswa}'

    class Meta:
         verbose_name_plural = 'Siswa'