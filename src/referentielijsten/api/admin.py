from urllib.parse import urlencode

from django.contrib import admin
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from referentielijsten.utils.admin import filter_title

from .admin_list_filters import GeldigListFilter
from .models import Item, Tabel


class ItemResource(resources.ModelResource):

    class Meta:
        model = Item


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ("naam", "code", "tabel", "is_geldig")
    list_filter = (
        GeldigListFilter,
        ("tabel__naam", filter_title("tabel naam")),
        ("tabel__code", filter_title("tabel code")),
    )
    fields = (
        "tabel",
        "code",
        "naam",
        "begindatum_geldigheid",
        "einddatum_geldigheid",
        "aanvullende_gegevens",
    )

    resource_classes = [ItemResource]

    @admin.display(description=_("Is geldig"), boolean=True)
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
    list_display = ("naam", "code", "is_geldig", "items_link")
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
            _("Beheerder"),
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

    @admin.display(description=_("Is geldig"), boolean=True)
    def is_geldig(self, obj):
        if not obj.einddatum_geldigheid or obj.einddatum_geldigheid > timezone.now():
            return True

        return False

    @admin.display(description=_("Actions"))
    def items_link(self, obj):
        url = (
            # TODO replace with reverse(..., query=...) once Django is upgraded to 5.2
            reverse("admin:api_item_changelist")
            + "?"
            + urlencode({"tabel__code": obj.code})
        )
        return format_html(
            '<a href="{}">{}</a>', url, _("Show items in item list view")
        )
