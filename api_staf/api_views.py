from rest_framework import viewsets
from api_staf.models import DataStaff, DataKelas, DataKeuangan
from api_staf.serializers import StaffSerializer as ss, KelasSerializer as ks, KeuanganSerializer as us


class StaffViewSets(viewsets.ModelViewSet):
    queryset = DataStaff.objects.all()
    serializer_class = ss
    lookup_field = "kd_staf"
    lookup_url_kwarg = "kd_staf"
    http_method_names = ['get']

class KelasViewsets(viewsets.ModelViewSet):
    queryset = DataKelas.objects.all()
    serializer_class = ks
    lookup_field = "kd_kelas"
    lookup_url_kwarg = "kd_kelas"
    http_method_names = ['get']


class KeuanganViewsets(viewsets.ModelViewSet):
    queryset = DataKeuangan.objects.all()
    serializer_class = us
    http_method_names = ['get']