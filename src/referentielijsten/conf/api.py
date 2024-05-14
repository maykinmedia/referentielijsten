from vng_api_common.conf.api import *  # noqa

# DRF
REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK["PAGE_SIZE"] = 100
REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = (
    "rest_framework.pagination.PageNumberPagination"
)
REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

SPECTACULAR_SETTINGS = {
    "SERVE_INCLUDE_SCHEMA": False,
    "CAMELIZE_NAMES": True,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
    ],
    "TITLE": "Referentielijsten API",
    "DESCRIPTION": "Een API om de informatie op te halen van stam tabellen",
    "CONTACT": {
        "url": "https://github.com/maykinmedia/referentielijsten",
    },
    "LICENSE": {
        "name": "EUPL",
        "url": "https://github.com/maykinmedia/referentielijsten/blob/master/LICENSE.md",
    },
    "VERSION": "1.0.0",
}
