from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

import structlog

from .metrics import (
    item_create_counter,
    item_delete_counter,
    item_update_counter,
    tabel_create_counter,
    tabel_delete_counter,
    tabel_update_counter,
)
from .models import Item, Tabel

logger = structlog.get_logger(__name__)


@receiver(post_save, sender=Tabel)
def log_tabel_save(sender, instance, created, **kwargs):
    logger.info(
        "tabel_created" if created else "tabel_updated",
        id=instance.id,
        code=instance.code,
        naam=instance.naam,
    )
    if created:
        tabel_create_counter.add(1)
    else:
        tabel_update_counter.add(1)


@receiver(post_delete, sender=Tabel)
def log_tabel_delete(sender, instance, **kwargs):
    logger.info(
        "tabel_deleted",
        id=instance.id,
        code=instance.code,
        naam=instance.naam,
    )
    tabel_delete_counter.add(1)


@receiver(post_save, sender=Item)
def log_item_save(sender, instance, created, **kwargs):
    logger.info(
        "item_created" if created else "item_updated",
        id=instance.id,
        code=instance.code,
        naam=instance.naam,
        tabel_code=instance.tabel.code if instance.tabel else None,
    )
    if created:
        item_create_counter.add(1)
    else:
        item_update_counter.add(1)


@receiver(post_delete, sender=Item)
def log_item_delete(sender, instance, **kwargs):
    logger.info(
        "item_deleted",
        id=instance.id,
        code=instance.code,
        naam=instance.naam,
        tabel_code=instance.tabel.code if instance.tabel else None,
    )
    item_delete_counter.add(1)
