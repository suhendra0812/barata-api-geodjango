from rest_framework_gis.filters import GeoFilterSet
from django_filters import rest_framework as filters

from boundaries.models import WPP
from .models import Ship


class ShipFilter(GeoFilterSet):
    wpp = filters.CharFilter(method="get_ship_by_wpp", lookup_expr="within")

    class Meta:
        model = Ship
        exclude = ["geom"]

    def get_ship_by_wpp(self, queryset, name, value):
        filtered_wpp = WPP.objects.filter(wpp=value)
        if filtered_wpp:
            wpp = filtered_wpp.first()
            ship_in_wpp = queryset.filter(geom__within=wpp.mpoly)
            return ship_in_wpp
