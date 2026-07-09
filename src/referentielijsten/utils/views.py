from drf_spectacular.views import (
    SpectacularJSONAPIView as _SpectacularJSONAPIView,
    SpectacularYAMLAPIView as _SpectacularYAMLAPIView,
)
from rest_framework.views import APIView


class AllowAllOriginsMixin(APIView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class SpectacularYAMLAPIView(AllowAllOriginsMixin, _SpectacularYAMLAPIView):
    """Spectacular YAML API view with Access-Control-Allow-Origin set to allow all"""


class SpectacularJSONAPIView(AllowAllOriginsMixin, _SpectacularJSONAPIView):
    """Spectacular JSON API view with Access-Control-Allow-Origin set to allow all"""
