from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from vng_api_common.serializers import GegevensGroepSerializer

from .models import Item, Tabel


class ValidationErrorSerializer(serializers.Serializer):
    """
    Validation error format, following the NL API Strategy.

    See https://docs.geostandaarden.nl/api/API-Strategie/ and
    https://docs.geostandaarden.nl/api/API-Strategie-ext/#error-handling-0
    """

    name = serializers.CharField(help_text=_("Name of the field with invalid data"))
    code = serializers.CharField(help_text=_("System code of the type of error"))
    reason = serializers.CharField(
        help_text=_("Explanation of what went wrong with the data")
    )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "code",
            "naam",
            "begindatum_geldigheid",
            "einddatum_geldigheid",
            "aanvullende_gegevens",
        )


class BeheerderSerializer(GegevensGroepSerializer):
    class Meta:
        model = Tabel
        gegevensgroep = "beheerder"


class TabelSerializer(serializers.ModelSerializer):
    beheerder = BeheerderSerializer(
        required=False,
        allow_null=True,
        help_text=_("De informatie van de beheerder van deze tabel."),
    )

    class Meta:
        model = Tabel
        fields = (
            "code",
            "naam",
            "beheerder",
            "einddatum_geldigheid",
        )
