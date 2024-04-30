from django.utils.translation import gettext_lazy as _

from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import ValidationError

from .filterset import ItemFilterset, TabelFilterset
from .models import Item, Tabel
from .serializers import ItemSerializer, TabelSerializer, ValidationErrorSerializer


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
                response=ValidationErrorSerializer,
                examples=[
                    OpenApiExample(
                        name="tabel__code query param not provided",
                        value={
                            "name": "tabel__code",
                            "code": "invalid",
                            "reason": _(
                                "Verplichte query parameter `tabel__code` niet mee gegeven."
                            ),
                        },
                    )
                ],
            ),
        },
    )
)
class ItemViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = "tabel__code"
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_url_kwargs = ["tabel__code", "is_geldig"]
    filterset_class = ItemFilterset

    def list(self, request, *args, **kwargs):
        code = request.query_params.get("tabel__code", None)
        if code is None:
            raise ValidationError(
                detail={
                    "tabel__code": _(
                        "Verplichte query parameter `tabel__code` niet mee gegeven."
                    ),
                }
            )

        return super().list(request, *args, **kwargs)


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
    lookup_field = "code"
    queryset = Tabel.objects.all()
    serializer_class = TabelSerializer
    lookup_url_kwargs = ["code", "is_geldig"]
    filterset_class = TabelFilterset
