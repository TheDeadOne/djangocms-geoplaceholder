# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from ipware.ip import get_ip
from django_geoip.models import IpRange

from .models import GeoPlaceholderModel
from .forms import GeoPlaceholderForm

class GeoPlaceholderPublisher(CMSPluginBase):
    model = GeoPlaceholderModel
    form = GeoPlaceholderForm
    name = _('Geo-targeting placeholder')
    render_template = "plugins/geo_placeholder.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(GeoPlaceholderPublisher, self).render(context, instance, placeholder)

        geo_placeholder_render = False
        if instance.country:
            attr_name = 'country'
        if instance.region:
            attr_name = 'region'
        if instance.city:
            attr_name = 'city'

        request = context['request']
        remote_addr = get_ip(request)
        if remote_addr:
            try:
                geoip_record = IpRange.objects.by_ip(remote_addr)
            except IpRange.DoesNotExist:
                pass
            else:
                if getattr(geoip_record, attr_name) == getattr(instance, attr_name):
                    geo_placeholder_render = True

        context.update({'geo_placeholder_render': geo_placeholder_render})
        return context


plugin_pool.register_plugin(GeoPlaceholderPublisher)
