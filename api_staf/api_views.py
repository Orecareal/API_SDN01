from rest_framework import viewsets
from api_staf.models import DataStaff, DataMapel
from api_staf.serializers import StaffSerializer as ss, MapelSerializer as ms


class StaffViewSets(viewsets.ModelViewSet):
    queryset = DataStaff.objects.all()
    serializer_class = ss


class MapelViewsets(viewsets.ModelViewSet):
    queryset = DataMapel.objects.all()
    serializer_class = ms