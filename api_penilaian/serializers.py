from rest_framework import serializers
from api_penilaian.models import DataAbsensiSiswa as dt_abs, DataNilaiSiswa as dt_nilai

class SiswaAbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = dt_abs
        fields = '__all__'


class NilaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = dt_nilai
        fields = '__all__'