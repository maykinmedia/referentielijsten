from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .filterset import TabelFilterset
from .serializers import TabelSerializer
from .models import Tabel


@extend_schema(
    tags=["tabelen"],
)
@extend_schema_view(
    list=extend_schema(
        operation_id="gettabelen",
        description="De operatie waarmee alle gegevens van een tabel wordt opgehaald.",
    ),
)
class TabelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tabel.objects.all()
    serializer_class = TabelSerializer
    filterset_class = TabelFilterset
    lookup_url_kwargs = ["code", "geldig"]
    lookup_field = "code"
