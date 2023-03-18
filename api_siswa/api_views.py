from api_siswa.serializers import SiswaSerializer as ss
from api_siswa.models import DataSiswa
from rest_framework import viewsets


class SiswaViewSets(viewsets.ModelViewSet):
    queryset = DataSiswa.objects.all()
    serializer_class = ss
    http_method_names = ['get', 'post']