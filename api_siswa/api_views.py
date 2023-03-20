from api_siswa.serializers import SiswaSerializer as ss
from api_siswa.models import DataSiswa
from rest_framework import viewsets


class SiswaViewSets(viewsets.ModelViewSet):
    queryset = DataSiswa.objects.all()
    serializer_class = ss
    lookup_field = "nis_siswa"
    lookup_url_kwarg = "nis_siswa"
    http_method_names = ['get']