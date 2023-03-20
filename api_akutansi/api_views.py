from rest_framework import viewsets
from api_akutansi.models import DataPembayaran
from api_akutansi.serializers import PembayaranSerializer


class PembayaranViewSets(viewsets.ModelViewSet):
    queryset = DataPembayaran.objects.all()
    serializer_class = PembayaranSerializer
    http_method_names = ['get']