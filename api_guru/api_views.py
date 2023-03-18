from rest_framework import viewsets
from api_guru.models import DataGuru, DataMapel, MapelGuru
from api_guru.serializers import GuruSerializers as gs, MapelSerializer as ms, MapelGuruSerializer as mgs


class GuruViewSets(viewsets.ModelViewSet):
    queryset = DataGuru.objects.all()
    serializer_class = gs
    http_method_names = ['get', 'post']


class MapelGuruViewsets(viewsets.ModelViewSet):
    queryset = MapelGuru.objects.all()
    serializer_class = mgs
    http_method_names = ['get', 'post']


class MapelViewsets(viewsets.ModelViewSet):
    queryset = DataMapel.objects.all()
    serializer_class = ms
    http_method_names = ['get', 'post']
    