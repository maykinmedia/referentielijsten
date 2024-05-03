from django.db import models
from django.utils import timezone


class ItemQuerySet(models.QuerySet):
    def geldig(self):
        return self.filter(
            (
                models.Q(begindatum_geldigheid__isnull=True)
                | models.Q(begindatum_geldigheid__lte=timezone.now())
            )
            & (
                models.Q(einddatum_geldigheid__isnull=True)
                | models.Q(einddatum_geldigheid__gt=timezone.now())
            )
        )

    def ongeldig(self):
        return self.filter(
            (
                models.Q(einddatum_geldigheid__lt=timezone.now())
                & models.Q(begindatum_geldigheid__gt=timezone.now())
            )
            | models.Q(einddatum_geldigheid__lt=timezone.now())
            | models.Q(begindatum_geldigheid__gt=timezone.now())
        )


class TabelQuerySet(models.QuerySet):
    def geldig(self):
        return self.filter(
            models.Q(einddatum_geldigheid__isnull=True)
            | models.Q(einddatum_geldigheid__gt=timezone.now())
        )

    def ongeldig(self):
        return self.filter(einddatum_geldigheid__lt=timezone.now())
