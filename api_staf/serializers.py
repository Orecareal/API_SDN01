from rest_framework import serializers
from api_staf.models import  DataStaff, DataKelas, DataKeuangan


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStaff
        fields = ('kd_staf', 'nm_staff', 'jen_kel', 'thn_aktif', 'thn_nonaktif')
        

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKelas
        fields = '__all__'


class KeuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKeuangan
        fields = '__all__'