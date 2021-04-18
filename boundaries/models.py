from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class WPP(models.Model):
    objectid = models.IntegerField(_("Object ID"))
    wpp = models.IntegerField(_("WPP Name"))
    mpoly = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "WPPs"

    def __str__(self):
        return str(self.wpp)
