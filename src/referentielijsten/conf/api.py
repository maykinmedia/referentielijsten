from vng_api_common.conf.api import *  # noqa

# DRF
REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK["PAGE_SIZE"] = 100
REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = (
    "rest_framework.pagination.PageNumberPagination"
)
REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "referentielijsten.utils.schema.AutoSchema"

SPECTACULAR_SETTINGS = {
    "REDOC_DIST": "SIDECAR",
    "SERVE_INCLUDE_SCHEMA": False,
    "CAMELIZE_NAMES": True,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
    ],
    "TITLE": "Referentielijsten API",
    "DESCRIPTION": "Een API om referentielijsten te raadplegen en de waarden te gebruiken in andere registraties.",
    "CONTACT": {
        "url": "https://github.com/maykinmedia/referentielijsten",
        "name": "Maykin Media",
        "email": "support@maykinmedia.nl",
    },
    "LICENSE": {
        "name": "EUPL",
        "url": "https://github.com/maykinmedia/referentielijsten/blob/master/LICENSE.md",
    },
    "VERSION": "0.1.0",
    "SERVERS": [{"url": "/api/v1"}],
}
