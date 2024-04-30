from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_filters.rest_framework import FilterSet, filters

from .models import Item, Tabel


class TabelFilterset(FilterSet):
    is_geldig = filters.BooleanFilter(
        help_text=_("Of de `einddatum_geldigheid` niet in het verleden ligt."),
        method="filter_is_geldig",
    )

    class Meta:
        model = Tabel
        fields = ("code", "is_geldig")

    def filter_is_geldig(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(einddatum_geldigheid__isnull=True)
                | Q(einddatum_geldigheid__gt=timezone.now())
            )
        return queryset.filter(einddatum_geldigheid__lt=timezone.now())


class ItemFilterset(FilterSet):
    is_geldig = filters.BooleanFilter(
        help_text=_(
            "Of de `begindatum_geldigheid` niet in de toekomst ligt en de `einddatum_geldigheid` "
            "niet in het verleden ligt."
        ),
        method="filter_is_geldig",
    )
    tabel__code = filters.CharFilter(
        help_text=_("De naam van de `tabel__code` gelinkt aan de items: VERPLICHT")
    )

    class Meta:
        model = Item
        fields = ("tabel__code", "is_geldig")

    def filter_is_geldig(self, queryset, name, value):
        if value:
            return queryset.filter(
                (
                    Q(begindatum_geldigheid__isnull=True)
                    | Q(begindatum_geldigheid__lte=timezone.now())
                )
                & (
                    Q(einddatum_geldigheid__isnull=True)
                    | Q(einddatum_geldigheid__gt=timezone.now())
                )
            )

        return queryset.filter(
            (
                Q(einddatum_geldigheid__lt=timezone.now())
                & Q(begindatum_geldigheid__gt=timezone.now())
            )
            | Q(einddatum_geldigheid__lt=timezone.now())
            | Q(begindatum_geldigheid__gt=timezone.now())
        )
