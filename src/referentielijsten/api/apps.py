from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "referentielijsten.api"

    def ready(self):
        from . import signals  # noqa: F401
