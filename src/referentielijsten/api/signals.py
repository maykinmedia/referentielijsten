from django.db.models.signals import post_save
from django.dispatch import receiver

import structlog

from .models import Item, Tabel

logger = structlog.get_logger()


@receiver(post_save, sender=Tabel)
def log_tabel_save(sender, instance, created, **kwargs):
    logger.info(
        "tabel_created" if created else "tabel_updated",
        id=instance.id,
        code=instance.code,
        naam=instance.naam,
    )


@receiver(post_save, sender=Item)
def log_item_save(sender, instance, created, **kwargs):
    logger.info(
        "item_created" if created else "item_updated",
        id=instance.id,
        code=instance.code,
        naam=instance.naam,
        tabel_code=instance.tabel.code if instance.tabel else None,
    )
