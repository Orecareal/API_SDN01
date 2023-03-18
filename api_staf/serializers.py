from rest_framework import serializers
from api_staf.models import  DataStaff, DataMapel


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStaff
        fields = ('kd_staf', 'nm_staff', 'jen_kel', 'thn_aktif', 'thn_nonaktif')


class MapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMapel
        fields = ('kd_mapel', 'nm_mapel', 'kkm_mapel')
