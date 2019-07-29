# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext as _

from django_geoip.models import City, Region, Country

from .models import GeoPlaceholderModel


class GeoPlaceholderForm(forms.ModelForm):
    country = forms.ModelChoiceField(label=GeoPlaceholderModel._meta.get_field('country').verbose_name.title(),
                                     queryset=Country.objects.order_by('name'), required=False)
    region = forms.ModelChoiceField(label=GeoPlaceholderModel._meta.get_field('region').verbose_name.title(),
                                    queryset=Region.objects.order_by('name'), required=False)
    city = forms.ModelChoiceField(label=GeoPlaceholderModel._meta.get_field('city').verbose_name.title(),
                                  queryset=City.objects.order_by('name'), required=False)

    class Meta:
        model = GeoPlaceholderModel
        exclude = []

    def clean(self):
        cleaned_data = super(GeoPlaceholderForm, self).clean()
        if sum(1 for v in cleaned_data.values() if v is None) != 2:
            raise forms.ValidationError(_('The one of country, region or city must be chosen!'))
        return cleaned_data
