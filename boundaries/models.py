from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

WPP_CHOICES = [
    (571, '571'),
    (572, '572'),
    (573, '573'),
    (711, '711'),
    (712, '712'),
    (713, '713'),
    (714, '714'),
    (715, '715'),
    (716, '716'),
    (717, '717'),
    (718, '718'),
]

class WPP(models.Model):
    objectid = models.IntegerField(_("Object ID"))
    wpp = models.IntegerField(_("WPP Name"), choices=WPP_CHOICES)
    mpoly = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "WPPs"

    def __str__(self):
        return str(self.wpp)
