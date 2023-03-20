from rest_framework import serializers
from api_penilaian.models import DataAbsensiSiswa as dt_abs, DataNilaiSiswa as dt_nilai

class SiswaAbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = dt_abs
        fields = ('kd_kelas', 'kd_mapel', 'keterangan', 'catatan')


class NilaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = dt_nilai
        fields = ('id_abs', 'test_type', 'nilai', 'catatan')