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
    ('1A', '1A'),('1B', '1B'),
    ('2A', '2A'),('2B', '2B'),
    ('3A', '3A'),('3B', '3B'),
    ('4A', '4A'),('4B', '4B'),
    ('5A', '5A'),('5B', '5B'),
    ('6A', '6A'),('6B', '6B'),
]

role_staff = [
    # 1 = Admin, 2 = Keuangan, 3 = Tata Usaha
    ('Admin', 'Admin'),
    ('Keuangan', 'Keuangan'),
    ('Tata Usaha', 'Tata Usaha'),
]

kategori_pbyr = [
    ('Reguler', 'Reguler'),
    ('Beasiswa', 'Beasiswa')
]

based_role = [
    ('Staff', 'Staff'),
    ('Guru', 'Guru'),
]

class DataStaff(models.Model):
    kd_staf = models.CharField(max_length=13, null=False, unique=True)
    role_staf = models.CharField(max_length=20, blank=True, choices=role_staff)
    nm_staff = models.CharField(max_length=100, null=False)
    jen_kel = models.CharField(max_length=12, choices=jen_kel)
    thn_aktif = models.DateField(default=datetime.datetime.now().strftime('%Y-%m-%d'))
    thn_nonaktif = models.DateField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.kd_staf} {self.nm_staff}"

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
        return f'{self.kd_kelas} | Pengajar : {self.id_guru}, | Siswa : {self.id_siswa}'
        
    class Meta:
         verbose_name_plural = 'Kelas'



class DataKeuangan(models.Model):
    # di db : 1 = Reguler, 2 = Beasiswa
    kategori = models.CharField(max_length=100, choices=kategori_pbyr)
    biaya = models.FloatField(default=0.00)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.kategori} : Rp. {self.biaya}"
        
    class Meta:
         verbose_name_plural = 'Keuangan'


class DataBerita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    author = models.ForeignKey(DataStaff, to_field="kd_staf", on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.judul} | by {self.author} | on {self.created}"
        
    class Meta:
         verbose_name_plural = 'Berita & Acara'


class DataGaji(models.Model):
    base_role = models.CharField(max_length=15, choices=based_role)
    gaji = models.CharField(max_length=10)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.base_role} / {self.gaji}"
        
    class Meta:
         verbose_name_plural = 'Gaji'