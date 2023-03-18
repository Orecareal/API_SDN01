from rest_framework import serializers
from api_staf.models import  DataStaff, DataMapel


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStaff
        fields = '__all__'


class MapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMapel
        fields = '__all__'
