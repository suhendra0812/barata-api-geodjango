from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class WPP(models.Model):
    objectid = models.IntegerField(_('Object ID'))
    wpp = models.CharField(_('WPP Name'), max_length=10)
    mpoly = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.wpp