from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .admin_list_filters import GeldigListFilter
from .models import Item, Tabel


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("tabel", "code", "naam", "is_geldig")
    list_filter = (GeldigListFilter, "tabel__code")
    fields = (
        "tabel",
        "code",
        "naam",
        "begindatum_geldigheid",
        "einddatum_geldigheid",
        "aanvullende_gegevens",
    )

    @admin.display(description="Is geldig", boolean=True)
    def is_geldig(self, obj):
        if (
            not obj.einddatum_geldigheid or obj.einddatum_geldigheid > timezone.now()
        ) and (
            not obj.begindatum_geldigheid or obj.begindatum_geldigheid <= timezone.now()
        ):
            return True

        return False


@admin.register(Tabel)
class TabelAdmin(admin.ModelAdmin):
    list_display = ("code", "naam", "is_geldig")
    list_filter = (GeldigListFilter,)

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "code",
                    "naam",
                    "einddatum_geldigheid",
                ]
            },
        ),
        (
            _("beheerder"),
            {
                "fields": [
                    "beheerder_naam",
                    "beheerder_email",
                    "beheerder_afdeling",
                    "beheerder_organisatie",
                ]
            },
        ),
    ]

    @admin.display(description="Is geldig", boolean=True)
    def is_geldig(self, obj):
        if not obj.einddatum_geldigheid or obj.einddatum_geldigheid > timezone.now():
            return True

        return False
