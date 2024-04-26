from django.contrib import admin

from .models import TokenAuth


@admin.register(TokenAuth)
class TokenAuthAdmin(admin.ModelAdmin):
    list_display = (
        "token",
        "contact_persoon",
        "organisatie",
        "administratie",
        "applicatie",
    )
    readonly_fields = ("token",)
