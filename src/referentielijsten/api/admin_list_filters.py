from django.contrib import admin
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class GeldigListFilter(admin.SimpleListFilter):
    title = _("Is geldig")
    parameter_name = "geldig"

    def lookups(self, request, model_admin):
        return (
            (True, "Ja"),
            (False, "Nee"),
        )


class ItemGeldigListFilter(GeldigListFilter):
    def queryset(self, request, queryset):
        if self.value() == "True":
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
        if self.value() == "False":
            return queryset.filter(
                (
                    Q(einddatum_geldigheid__lt=timezone.now())
                    & Q(begindatum_geldigheid__gt=timezone.now())
                )
                | Q(einddatum_geldigheid__lt=timezone.now())
                | Q(begindatum_geldigheid__gt=timezone.now())
            )

        return queryset


class TabelGeldigListFilter(GeldigListFilter):
    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(
                Q(einddatum_geldigheid__isnull=True)
                | Q(einddatum_geldigheid__gt=timezone.now())
            )
        if self.value() == "False":
            return queryset.filter(einddatum_geldigheid__lt=timezone.now())

        return queryset
