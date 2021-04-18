from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Ship


class ShipSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ship
        geo_field = "geom"
        fields = "__all__"
