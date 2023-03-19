from api_penilaian.serializers import SiswaAbsensiSerializer as abs ,NilaiSerializer as ns
from api_penilaian.models import DataAbsensiSiswa, DataNilaiSiswa
from rest_framework import viewsets


class SiswaAbsensiViewSets(viewsets.ModelViewSet):
    queryset = DataAbsensiSiswa.objects.all()
    serializer_class = abs
    http_method_names = ['get']


class NilaiSiswaViewSets(viewsets.ModelViewSet):
    queryset = DataNilaiSiswa.objects.all()
    serializer_class = ns
    http_method_names = ['get']