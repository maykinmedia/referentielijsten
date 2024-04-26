import binascii
import os

from django.db import models
from django.utils.translation import gettext_lazy as _


class TokenAuth(models.Model):
    token = models.CharField(_("token"), max_length=40)
    contact_persoon = models.CharField(
        _("contact persoon"),
        max_length=200,
        help_text=_(
            "De naam van de contact persoon van de organisatie die gebruik mag maken van de API."
        ),
    )
    email = models.EmailField(
        _("email"),
        help_text=_("De email van de oranisatie die gebruik mag maken van de API."),
    )
    afdeling = models.CharField(
        _("afdeling"),
        max_length=200,
        blank=True,
        help_text=_("De afdeling van de organisatie die gebruik mag maken van de API."),
    )
    organisatie = models.CharField(
        _("organisatie"),
        max_length=200,
        blank=True,
        help_text=_("De organisatie die gebruik mag maken van de API"),
    )
    laatst_aangepast = models.DateTimeField(
        _("laatst aangepast"),
        auto_now=True,
        help_text=_("De laatste datum dat de token aangepast was."),
    )
    aangemaakt = models.DateTimeField(
        _("created"),
        auto_now_add=True,
        help_text=_("De datum wanneer de token was aangemaakt."),
    )
    applicatie = models.CharField(
        _("application"),
        max_length=200,
        blank=True,
        help_text=_("De applicatie die gebruik mag maken van de API."),
    )
    administratie = models.CharField(
        _("administration"),
        max_length=200,
        blank=True,
        help_text=_("De administratie die gebruik mag maken van de API."),
    )

    class Meta:
        verbose_name = _("token authorizatie")
        verbose_name_plural = _("token authorizaties")

    def __str__(self):
        return self.naam

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super().save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()
