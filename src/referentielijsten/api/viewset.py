from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets

from .filterset import TabelFilterset
from .models import Tabel
from .serializers import TabelSerializer


@extend_schema(
    tags=["tabelen"],
)
@extend_schema_view(
    list=extend_schema(
        operation_id="gettabelen",
        description="De operatie waarmee alle gegevens van een tabel wordt opgehaald.",
    ),
)
class TabelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = "code"
    queryset = Tabel.objects.all()
    serializer_class = TabelSerializer
    lookup_url_kwargs = ["code", "geldig"]
    filterset_class = TabelFilterset

    def get_queryset(self):
        code = self.request.query_params.get("code", None)
        if code is None:
            return Tabel.objects.none()

        return Tabel.objects.filter(code=code)
