from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Ship


class ShipAdmin(LeafletGeoAdmin):
    list_display = [
        "vessel_id",
        "vessel_name",
        "lon",
        "lat",
        "datetime",
        "length",
        "status",
    ]


admin.site.register(Ship, ShipAdmin)
