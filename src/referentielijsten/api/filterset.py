from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_filters.rest_framework import FilterSet, filters

from .models import Tabel


class TabelFilterset(FilterSet):
    geldig = filters.BooleanFilter(
        help_text=_("Zoek klantcontacten met specifieke tekst in inhoud"),
        method="filter_geldig",
    )

    class Meta:
        model = Tabel
        fields = ("code", "geldig")

    def filter_geldig(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(einddatum_geldigheid__isnull=True)
                | Q(einddatum_geldigheid__gt=timezone.now())
            )
        return queryset.filter(einddatum_geldigheid__lt=timezone.now())
