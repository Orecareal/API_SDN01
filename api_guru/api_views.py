from rest_framework import viewsets
from api_guru.models import DataGuru, MapelGuru
from api_guru.serializers import GuruSerializers as gs, MapelGuruSerializer as mgs


class GuruViewSets(viewsets.ModelViewSet):
    queryset = DataGuru.objects.all()
    serializer_class = gs
    http_method_names = ['get', 'post']


class MapelGuruViewsets(viewsets.ModelViewSet):
    queryset = MapelGuru.objects.all()
    serializer_class = mgs
    http_method_names = ['get', 'post']