from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "referentielijsten.utils"

    def ready(self):
        from . import checks, query  # noqa
