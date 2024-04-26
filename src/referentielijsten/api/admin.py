from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.utils import timezone

from .models import Tabel, Item


class ItemInlineAdmin(admin.TabularInline):
    model = Item
    extra = 1
    fields = (
        "code",
        "naam",
        "begindatum_geldigheid",
        "einddatum_geldigheid",
        "aanvullende_gegevens",
    )


@admin.register(Tabel)
class TabelAdmin(admin.ModelAdmin):
    list_display = ("code", "naam", "is_geldig")
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
    inlines = (ItemInlineAdmin,)

    @admin.display(description="Is geldig", boolean=True)
    def is_geldig(self, obj):
        if not obj.einddatum_geldigheid or obj.einddatum_geldigheid > timezone.now():
            return True

        return False
