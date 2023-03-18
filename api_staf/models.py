from django.db import models
import datetime

# Create your models here.


jen_kel = [
    ('L', 'Laki-laki'),
    ('P', 'Perempuan')
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
        


class DataMapel(models.Model):
    kd_mapel = models.CharField(max_length=13, null=False, unique=True)
    nm_mapel = models.CharField(max_length=100, null=False)
    kkm_mapel = models.FloatField(max_length=3, default=7.00)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.kd_mapel} - {self.nm_mapel}'
        
    class Meta:
         verbose_name_plural = 'Mapel'