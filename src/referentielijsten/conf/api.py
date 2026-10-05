from vng_api_common.conf.api import *  # type: ignore # noqa

API_VERSION = "0.2.0"


# DRF
REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK["PAGE_SIZE"] = 100
REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = (
    "vng_api_common.pagination.DynamicPageSizePagination"
)
REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "referentielijsten.utils.schema.AutoSchema"

# TODO should be addressed in commonground-api-common
# See: https://github.com/maykinmedia/commonground-api-common/issues/190
# DRF 3.18 changed the default list-serializer error format from a list to a
# dict keyed by index. `vng_api_common`'s exception handler still expects the
# list-based format to build indexed `invalidParams` paths, so keep the old format until that's updated.
REST_FRAMEWORK["LIST_SERIALIZER_ERRORS_AS_DICT"] = False

SPECTACULAR_SETTINGS = {
    "REDOC_DIST": "SIDECAR",
    "SERVE_INCLUDE_SCHEMA": False,
    "CAMELIZE_NAMES": True,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
        "maykin_common.drf_spectacular.hooks.remove_invalid_url_defaults",
    ],
    "TITLE": "Referentielijsten API",
    "DESCRIPTION": "Een API om referentielijsten te raadplegen en de waarden te gebruiken in andere registraties.",
    "CONTACT": {
        "url": "https://github.com/maykinmedia/referentielijsten",
        "name": "Maykin",
        "email": "support@maykin.nl",
    },
    "LICENSE": {
        "name": "EUPL",
        "url": "https://github.com/maykinmedia/referentielijsten/blob/master/LICENSE.md",
    },
    "VERSION": API_VERSION,
    "SERVERS": [{"url": "/api/v1"}],
}
