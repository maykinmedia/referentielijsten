from distutils.util import strtobool

from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from rest_framework import serializers
from vng_api_common.serializers import GegevensGroepSerializer

from .models import Tabel, Item


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
    items = serializers.SerializerMethodField()
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
            "items",
        )

    def get_items(self, obj):
        request = self.context["request"]
        geldig = request.query_params.get("geldig", "false")
        if strtobool(geldig):
            item_qs = obj.item_set.filter(
                Q(begindatum_geldigheid__isnull=True)
                | Q(begindatum_geldigheid__lt=timezone.now())
                & Q(einddatum_geldigheid__isnull=True)
                | Q(einddatum_geldigheid__gt=timezone.now())
            )
            return ItemSerializer(item_qs, many=True).data

        return ItemSerializer(obj.item_set.all(), many=True).data
