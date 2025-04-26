from rest_framework import response
from rest_framework.viewsets import ModelViewSet
from category.models import Region
from .serializers import RegionSerializer

class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer