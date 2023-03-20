from rest_framework import serializers
from api_guru.models import DataGuru, MapelGuru, DataMapel, DataKonseling

class GuruSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataGuru
        fields = ('kd_guru', 'nm_guru', 'jen_kel', 'jbt_guru')


class MapelGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapelGuru
        fields = ('id_guru', 'id_mapel')



class MapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMapel
        fields = ('kd_mapel', 'nm_mapel', 'kkm_mapel')


class KonselingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKonseling
        fields = '__all__'