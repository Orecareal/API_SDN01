from django.db import models
from api_siswa.models import DataSiswa
from api_staf.models import DataStaff, DataKeuangan
from api_guru.models import DataGuru

import datetime

# Create your models here.
class DataPembayaran(models.Model):
    kd_siswa = models.ForeignKey(DataSiswa, to_field="nis_siswa", blank=True, null=True, on_delete=models.CASCADE)
    jenis_pby = models.ForeignKey(DataKeuangan, blank=True, null=True, on_delete=models.CASCADE)
    jml_bayar = models.CharField(max_length=30, null=False, default='-')
    status = models.CharField(max_length=15, choices=[('Lunas', 'Lunas'), ('Belum Lunas', 'Belum Lunas')])
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.kd_siswa} | {self.jml_bayar} | {self.status}"

    class Meta:
         verbose_name_plural = 'Pembayaran Siswa'


class GajiStaff(models.Model):
    id_staff = models.ForeignKey(DataStaff, to_field="kd_staf", blank=True, null=True, on_delete=models.CASCADE)
    jml_bayar = models.CharField(max_length=30, null=False, default='-')
    status = models.CharField(max_length=15, choices=[('Sudah Dibayar', 'Sudah Dibayar'), ('Tertunda', 'Tertunda')])
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.id_staff} | {self.jml_bayar} | {self.status}"
        
    class Meta:
         verbose_name_plural = 'Gaji Staff'


class GajiGuru(models.Model):
    id_guru = models.ForeignKey(DataGuru, to_field="kd_guru", blank=True, null=True, on_delete=models.CASCADE)
    jml_bayar = models.CharField(max_length=30, null=False, default='-')
    status = models.CharField(max_length=15, choices=[('Sudah Dibayar', 'Sudah Dibayar'), ('Tertunda', 'Tertunda')])
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.id_guru} | {self.jml_bayar} | {self.status}"
        
    class Meta:
         verbose_name_plural = 'Gaji Guru'
