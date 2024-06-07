from django.conf import settings as django_settings


def settings(request):
    public_settings = (
        "GOOGLE_ANALYTICS_ID",
        "ENVIRONMENT",
        "ENVIRONMENT_SHOWN_IN_ADMIN",
        "PROJECT_NAME",
    )

    context = {
        "settings": {k: getattr(django_settings, k, None) for k in public_settings},
    }

    if hasattr(django_settings, "SENTRY_CONFIG"):
        context.update(dsn=django_settings.SENTRY_CONFIG.get("public_dsn", ""))

    return context
