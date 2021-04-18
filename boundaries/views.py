from django.contrib.gis.db.models.functions import Area
from rest_framework import viewsets

from .models import WPP
from .serializers import WPPSerializer


class WPPViewSet(viewsets.ModelViewSet):
    queryset = WPP.objects.all()
    serializer_class = WPPSerializer

    def get_queryset(self):
        wpp_area = WPP.objects.annotate(area=Area("mpoly")).order_by("area")
        return wpp_area
