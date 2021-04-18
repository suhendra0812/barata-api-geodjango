from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import WPP


class WPPAdmin(LeafletGeoAdmin):
    list_display = [
        "pk",
        "wpp",
    ]

    list_display_links = ["wpp"]


admin.site.register(WPP, WPPAdmin)
