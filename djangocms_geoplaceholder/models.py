# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from django_geoip.models import City, Region, Country


@python_2_unicode_compatible
class GeoPlaceholderModel(CMSPlugin):
    country = models.ForeignKey(Country, verbose_name=_('Country'), null=True, blank=True, on_delete=models.SET_NULL)
    region = models.ForeignKey(Region, verbose_name=_('Region'), null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, verbose_name=_('City'), null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        location = self.country or self.region or self.city
        return u'{}'.format(location)
