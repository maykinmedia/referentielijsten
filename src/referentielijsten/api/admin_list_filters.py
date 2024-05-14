from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class GeldigListFilter(admin.SimpleListFilter):
    title = _("Is geldig")
    parameter_name = "geldig"

    def lookups(self, request, model_admin):
        return (
            (True, "Ja"),
            (False, "Nee"),
        )

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.geldig()
        if self.value() == "False":
            return queryset.ongeldig()
        return queryset
