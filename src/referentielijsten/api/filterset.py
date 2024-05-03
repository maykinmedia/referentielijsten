from django.utils.translation import gettext_lazy as _

from django_filters.rest_framework import FilterSet, filters

from .models import Item, Tabel


class TabelFilterset(FilterSet):
    code = filters.CharFilter(
        help_text=_("De waarde van de `code` van een specifieke `tabel`.")
    )

    is_geldig = filters.BooleanFilter(
        help_text=_("Of de `einddatum_geldigheid` niet in het verleden ligt."),
        method="filter_is_geldig",
    )

    class Meta:
        model = Tabel
        fields = ("code", "is_geldig")

    def filter_is_geldig(self, queryset, name, value):
        if value:
            return queryset.geldig()
        return queryset.ongeldig()


class ItemFilterset(FilterSet):
    is_geldig = filters.BooleanFilter(
        help_text=_(
            "Of de `begindatum_geldigheid` niet in de toekomst ligt en de `einddatum_geldigheid` "
            "niet in het verleden ligt."
        ),
        method="filter_is_geldig",
    )
    tabel__code = filters.CharFilter(
        help_text=_(
            "De waarde van de `tabel__code` die gelinkt is aan de items: VERPLICHT"
        ),
        required=True,
    )

    class Meta:
        model = Item
        fields = ("tabel__code", "is_geldig")

    def filter_is_geldig(self, queryset, name, value):
        if value:
            return queryset.geldig()
        return queryset.ongeldig()
