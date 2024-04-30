from django.db import models
from django.utils.translation import gettext_lazy as _

from vng_api_common.descriptors import GegevensGroepType


class Tabel(models.Model):
    code = models.CharField(
        _("code"),
        help_text=_("De unique code van het tabel."),
        max_length=40,
        unique=True,
    )
    naam = models.CharField(
        _("naam"),
        help_text=_("De naam van het tabel."),
        max_length=200,
    )
    einddatum_geldigheid = models.DateTimeField(
        _("einddatum geldigheid"),
        help_text=_("De datum tot wanneer deze tabel geldig is."),
        editable=True,
        blank=True,
        null=True,
    )

    # Beheerder gegevens groep
    beheerder_naam = models.CharField(
        _("naam"),
        max_length=200,
        help_text=_("De naam van de beheerder van dit tabel."),
        blank=True,
        null=True,
    )
    beheerder_email = models.EmailField(
        _("mail"),
        help_text=_("De email van de beheerder van dit tabel."),
        blank=True,
        null=True,
    )
    beheerder_afdeling = models.CharField(
        _("afdeling"),
        max_length=200,
        help_text=_("De afdelings naam van de beheerder van dit tabel."),
        blank=True,
        null=True,
    )
    beheerder_organisatie = models.CharField(
        _("organisatie"),
        max_length=200,
        help_text=_("De organisatie naam van de beheerder van dit tabel."),
        blank=True,
        null=True,
    )
    beheerder = GegevensGroepType(
        {
            "naam": beheerder_naam,
            "email": beheerder_email,
            "afdeling": beheerder_afdeling,
            "organisatie": beheerder_organisatie,
        },
        optional=(
            "naam",
            "email",
            "afdeling",
            "organisatie",
        ),
    )

    class Meta:
        verbose_name = _("tabel")
        verbose_name_plural = _("tabellen")

    def __str__(self):
        return str(self.code)


class Item(models.Model):
    tabel = models.ForeignKey(
        Tabel,
        verbose_name=_("tabel"),
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        _("code"),
        help_text=_("De unique code (per tabel) van het item."),
        max_length=36,
    )
    naam = models.CharField(
        _("naam"),
        help_text=_("De naam van het item."),
        max_length=200,
    )
    begindatum_geldigheid = models.DateTimeField(
        _("begindatum geldigheid"),
        help_text=_("De datum vanaf waneer deze tabel geldig is."),
        editable=True,
        blank=True,
        null=True,
    )
    einddatum_geldigheid = models.DateTimeField(
        _("einddatum geldigheid"),
        help_text=_("De datum tot wanneer deze tabel geldig is."),
        editable=True,
        blank=True,
        null=True,
    )
    aanvullende_gegevens = models.JSONField(
        _("aanvullende gegevens"),
        help_text=_("Extra gegevens die niet standaard gekoppeld zijn aan een item."),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
        unique_together = ("tabel", "code")

    def __str__(self):
        return f"{self.tabel.code} - {self.code}"
