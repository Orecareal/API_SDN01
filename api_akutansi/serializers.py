from rest_framework import serializers
from api_akutansi.models import DataPembayaran, GajiStaff, GajiGuru

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPembayaran
        fields = ('kd_siswa', 'jenis_pby', 'jml_bayar', 'status', 'created')


class GajiStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = GajiStaff
        fields = ('id_staff', 'jml_bayar', 'status', 'created')


class GajiGUruSerializer(serializers.ModelSerializer):
    class Meta:
        model = GajiGuru
        fields = ('id_guru', 'jml_bayar', 'status', 'created')