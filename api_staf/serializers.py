from rest_framework import serializers
from api_staf.models import  DataStaff, DataKelas


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStaff
        fields = ('kd_staf', 'nm_staff', 'jen_kel', 'thn_aktif', 'thn_nonaktif')
        

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKelas
        fields = '__all__'
