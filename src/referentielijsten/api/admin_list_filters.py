from django.contrib import admin
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from .managers import ItemQuerySet


class GeldigListFilter(admin.SimpleListFilter):
    title = _("Is geldig")
    parameter_name = "geldig"

    def lookups(self, request, model_admin) -> tuple:
        return (
            (True, "Ja"),
            (False, "Nee"),
        )

    def queryset(self, request: HttpRequest, queryset: ItemQuerySet) -> ItemQuerySet:  # pyright: ignore[reportIncompatibleMethodOverride]
        if self.value() == "True":
            return queryset.geldig()
        if self.value() == "False":
            return queryset.ongeldig()
        return queryset
