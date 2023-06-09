from rest_framework import serializers
from api_staf.models import  DataStaff, DataKelas, DataKeuangan, DataBerita, DataGaji


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStaff
        fields = ('kd_staf', 'nm_staff', 'jen_kel', 'thn_aktif', 'thn_nonaktif')
        

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKelas
        fields = ('kd_kelas', 'id_guru', 'id_siswa', 'lama_jam')


class KeuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKeuangan
        fields = ('kategori', 'biaya')


class BeritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBerita
        fields = ('judul', 'isi', 'author')


class GajiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataGaji
        fields = ('base_role', 'gaji')