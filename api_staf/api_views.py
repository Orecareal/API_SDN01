from rest_framework import viewsets, generics
from api_staf.models import DataStaff, DataKelas
from api_staf.serializers import StaffSerializer as ss, KelasSerializer as ks


class StaffViewSets(viewsets.ModelViewSet):
    queryset = DataStaff.objects.all()
    serializer_class = ss
    lookup_field = "kd_staf"
    lookup_url_kwarg = "kd_staf"
    http_method_names = ['get', 'post']

class KelasViewsets(viewsets.ModelViewSet):
    queryset = DataKelas.objects.all()
    serializer_class = ks
    http_method_names = ['get', 'post']


