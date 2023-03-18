from rest_framework import serializers
from api_siswa.models import DataSiswa


class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSiswa
        fields = ('nis_siswa', 'nm_siswa', 'jen_kel', 'alamat', 'no_telp')