from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Ship(models.Model):
    vessel_id = models.CharField(_("Vessel ID"), max_length=100)
    vessel_name = models.CharField(_("Vessel Name"), max_length=100)
    lon = models.FloatField(_("Longitude"))
    lat = models.FloatField(_("Latitude"))
    datetime = models.DateTimeField(_("Datetime"))
    length = models.FloatField(_("Length"))
    status = models.CharField(_("Status"), max_length=5)

    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.vessel_name
