from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WPP

wpp_mapping = {
    "objectid": "OBJECTID",
    "wpp": "WPP",
    "mpoly": "MULTIPOLYGON",
}

wpp_shp = Path(__file__).resolve().parent / "data" / "WPP_Full_PermenKP182014.shp"


def run(verbose=True):
    lm = LayerMapping(WPP, str(wpp_shp), wpp_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
