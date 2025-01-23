from django.utils.translation import gettext_lazy as _

from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import mixins, status, viewsets
from vng_api_common.serializers import FieldValidationErrorSerializer

from .filterset import ItemFilterset, TabelFilterset
from .models import Item, Tabel
from .serializers import ItemSerializer, TabelSerializer


@extend_schema(
    tags=["items"],
)
@extend_schema_view(
    list=extend_schema(
        operation_id="getitems",
        description="De operatie waarmee alle items van een tabel wordt opgehaald.",
        responses={
            200: ItemSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=FieldValidationErrorSerializer,
                examples=[
                    OpenApiExample(
                        name="tabel__code query param not provided",
                        value={
                            "name": "tabel__code",
                            "code": "required",
                            "reason": _("Dit veld is vereist."),
                        },
                    )
                ],
            ),
        },
    )
)
class ItemViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Item.objects.order_by("-pk")
    serializer_class = ItemSerializer
    filterset_class = ItemFilterset


@extend_schema(
    tags=["tabellen"],
)
@extend_schema_view(
    list=extend_schema(
        operation_id="gettabellen",
        description="De operatie waarmee alle gegevens van een tabel wordt opgehaald.",
    ),
)
class TabelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tabel.objects.order_by("-pk")
    serializer_class = TabelSerializer
    filterset_class = TabelFilterset
