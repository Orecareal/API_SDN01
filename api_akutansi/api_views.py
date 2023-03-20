from rest_framework import viewsets
from api_akutansi.models import DataPembayaran, GajiStaff, GajiGuru
from api_akutansi.serializers import PembayaranSerializer as ps,\
GajiGUruSerializer as ggs, GajiStaffSerializer as gss


class PembayaranViewSets(viewsets.ModelViewSet):
    queryset = DataPembayaran.objects.all()
    serializer_class = ps
    http_method_names = ['get']


class GajiStaffViewSets(viewsets.ModelViewSet):
    queryset = GajiStaff.objects.all()
    serializer_class = gss
    http_method_names = ['get']



class GajiGuruViewSets(viewsets.ModelViewSet):
    queryset = GajiGuru.objects.all()
    serializer_class = ggs
    http_method_names = ['get']