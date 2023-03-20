from rest_framework import serializers
from api_akutansi.models import DataPembayaran

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPembayaran
        fields = '__all__'