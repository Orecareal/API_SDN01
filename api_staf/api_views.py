from rest_framework import viewsets
from api_staf.models import DataStaff, DataKelas, DataKeuangan, DataBerita
from api_staf.serializers import StaffSerializer as ss, KelasSerializer as ks, \
KeuanganSerializer as us, BeritaSerializer as bs


class StaffViewSets(viewsets.ModelViewSet):
    queryset = DataStaff.objects.all()
    serializer_class = ss
    lookup_field = "kd_staf"
    lookup_url_kwarg = "kd_staf"
    http_method_names = ['get']

class KelasViewsets(viewsets.ModelViewSet):
    queryset = DataKelas.objects.all()
    serializer_class = ks
    http_method_names = ['get']


class KeuanganViewsets(viewsets.ModelViewSet):
    queryset = DataKeuangan.objects.all()
    serializer_class = us
    http_method_names = ['get']


class BeritaViewsets(viewsets.ModelViewSet):
    queryset = DataBerita.objects.all()
    serializer_class = bs
    http_method_names = ['get']