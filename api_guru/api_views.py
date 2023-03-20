from rest_framework import viewsets
from api_guru.models import DataGuru, DataMapel, MapelGuru, DataKonseling
from api_guru.serializers import GuruSerializers as gs, MapelSerializer as ms, \
MapelGuruSerializer as mgs, KonselingSerializer as ks


class GuruViewSets(viewsets.ModelViewSet):
    queryset = DataGuru.objects.all()
    serializer_class = gs
    lookup_field = "kd_guru"
    lookup_url_kwarg = "kd_guru"
    http_method_names = ['get']


class MapelGuruViewsets(viewsets.ModelViewSet):
    queryset = MapelGuru.objects.all()
    serializer_class = mgs
    http_method_names = ['get']


class MapelViewsets(viewsets.ModelViewSet):
    queryset = DataMapel.objects.all()
    serializer_class = ms
    lookup_field = "kd_mapel"
    lookup_url_kwarg = "kd_mapel"
    http_method_names = ['get']
    

class KonselingViewsets(viewsets.ModelViewSet):
    queryset = DataKonseling.objects.all()
    serializer_class = ks
    http_method_names = ['get']
    