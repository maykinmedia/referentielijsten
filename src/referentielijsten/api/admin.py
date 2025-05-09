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
from .forms import ItemConfirmImportForm, ItemImportForm
from .models import Item, Tabel


class ItemInline(admin.StackedInline):
    model = Item
    extra = 1
    fields = (
        "code",
        "naam",
        "begindatum_geldigheid",
        "einddatum_geldigheid",
        "aanvullende_gegevens",
    )


class ItemResource(resources.ModelResource):
    def __init__(self, *args, selected_tabel=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected_tabel = selected_tabel

    def before_import_row(self, row, **kwargs):
        if self.selected_tabel:
            row["tabel"] = self.selected_tabel.id

    class Meta:
        model = Item
        import_id_fields = ("code",)


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ("naam", "code", "tabel", "is_geldig")
    list_filter = (
        GeldigListFilter,
        ("tabel__naam", filter_title("tabel naam")),
    )
    fields = (
        "tabel",
        "code",
        "naam",
        "begindatum_geldigheid",
        "einddatum_geldigheid",
        "aanvullende_gegevens",
    )
    import_form_class = ItemImportForm
    confirm_form_class = ItemConfirmImportForm
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

    def get_confirm_form_initial(self, request, import_form):
        initial = super().get_confirm_form_initial(request, import_form)
        if import_form and import_form.is_valid():
            initial["selected_tabel"] = import_form.cleaned_data.get("selected_tabel")
        return initial

    def get_import_resource_kwargs(self, request, form=None):
        resource_kwargs = super().get_import_resource_kwargs(request, form=form)
        if form and form.is_valid():
            resource_kwargs["selected_tabel"] = form.cleaned_data.get("selected_tabel")
        return resource_kwargs


@admin.register(Tabel)
class TabelAdmin(admin.ModelAdmin):
    list_display = ("naam", "code", "is_geldig", "items_link")
    list_filter = (GeldigListFilter,)
    inlines = [ItemInline]

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
            reverse("admin:api_item_changelist")
            + "?"
            + urlencode({"tabel__id": obj.id})
        )
        return format_html(
            '<a href="{}">{}</a>', url, _("Show items in item list view")
        )
