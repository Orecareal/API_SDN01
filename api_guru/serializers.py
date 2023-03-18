from rest_framework import serializers
from api_guru.models import DataGuru, MapelGuru

class GuruSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataGuru
        fields = ('kd_guru', 'nm_guru', 'jen_kel', 'jbt_guru')


class MapelGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapelGuru
        fields = ('id_guru', 'id_mapel')


# class GuruDetailSerializer(serializers.ModelSerializer):
#     guru = GuruSerializers()
#     mapel = MapelGuruSerializer()
#     detail = serializers.SerializerMethodField()

#     class Meta:
#         model = DataGuru
#         fields = '__all__'
    
#     def get_detail():
#         return{
#             'Nama_guru':'obj.nm_guru',
#         }