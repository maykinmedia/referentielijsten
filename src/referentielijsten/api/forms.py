from django import forms
from django.utils.translation import gettext_lazy as _

from import_export.forms import ConfirmImportForm, ImportForm

from .models import Tabel


class ItemImportForm(ImportForm):
    selected_tabel = forms.ModelChoiceField(
        queryset=Tabel.objects.all(),
        label="Tabel",
        required=False,
        help_text=_(
            "Selecteer een tabel voor alle geïmporteerde items. "
            "Als je hier een tabel selecteert, wordt een eventuele 'table_id' in het bestand genegeerd."
        ),
    )


class ItemConfirmImportForm(ConfirmImportForm):
    selected_tabel = forms.ModelChoiceField(
        queryset=Tabel.objects.all(),
        required=False,
        widget=forms.HiddenInput(),
    )
