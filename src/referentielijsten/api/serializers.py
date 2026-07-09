from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from vng_api_common.serializers import GegevensGroepSerializer

from .models import Item, Tabel


class ItemSerializer(serializers.ModelSerializer[Item]):
    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Item
        fields = (
            "code",
            "naam",
            "begindatum_geldigheid",
            "einddatum_geldigheid",
            "aanvullende_gegevens",
        )


class BeheerderSerializer(GegevensGroepSerializer):
    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Tabel
        gegevensgroep = "beheerder"


class TabelSerializer(serializers.ModelSerializer[Tabel]):
    beheerder = BeheerderSerializer(
        required=False,
        allow_null=True,
        help_text=_("De informatie van de beheerder van deze tabel."),
    )

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Tabel
        fields = (
            "code",
            "naam",
            "beheerder",
            "einddatum_geldigheid",
        )
