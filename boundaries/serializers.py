from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import WPP


class WPPSerializer(GeoFeatureModelSerializer):
    area = serializers.CharField(max_length=100)

    class Meta:
        model = WPP
        geo_field = "mpoly"
        fields = "__all__"
