from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Ship

ship_mapping = {
    "vessel_id": "vessel_id",
    "vessel_name": "vessel_name",
    "lon": "lon",
    "lat": "lat",
    "datetime": "datetime",
    "length": "length",
    "status": "status",
    "geom": "POINT",
}

ship_shp = Path(__file__).resolve().parent / "data" / "ship_list.geojson"


def run(verbose=True):
    lm = LayerMapping(Ship, str(ship_shp), ship_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)