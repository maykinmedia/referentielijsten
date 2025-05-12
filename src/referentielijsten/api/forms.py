from import_export.forms import ImportForm, ConfirmImportForm
from django import forms
from .models import Tabel


class ItemImportForm(ImportForm):
    selected_tabel = forms.ModelChoiceField(
        queryset=Tabel.objects.all(),
        label="Tabel",
        required=False,
        help_text="Selecteer een tabel om toe te passen op alle geïmporteerde items, "
        "tenzij de tabel al is aangegeven in het bestand.",
    )


class ItemConfirmImportForm(ConfirmImportForm):
    selected_tabel = forms.ModelChoiceField(
        queryset=Tabel.objects.all(), label="Tabel", required=False
    )
