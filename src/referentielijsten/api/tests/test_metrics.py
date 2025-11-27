# SPDX-License-Identifier: EUPL-1.2
from unittest.mock import MagicMock, patch

from django.test import TestCase

from ..metrics import (
    item_create_counter,
    item_delete_counter,
    item_update_counter,
    tabel_create_counter,
    tabel_delete_counter,
    tabel_update_counter,
)
from .factories import ItemFactory, TabelFactory


class TabelMetricsTests(TestCase):
    @patch.object(tabel_create_counter, "add", wraps=tabel_create_counter.add)
    def test_tabel_create_metric(self, mock_add: MagicMock):
        TabelFactory.create()
        mock_add.assert_called_once_with(1)

    @patch.object(tabel_update_counter, "add", wraps=tabel_update_counter.add)
    def test_tabel_update_metric(self, mock_add: MagicMock):
        tabel = TabelFactory.create()
        tabel.naam = "Updated name"
        tabel.save()
        mock_add.assert_called_once_with(1)

    @patch.object(tabel_delete_counter, "add", wraps=tabel_delete_counter.add)
    def test_tabel_delete_metric(self, mock_add: MagicMock):
        tabel = TabelFactory.create()
        tabel.delete()
        mock_add.assert_called_once_with(1)


class ItemMetricsTests(TestCase):
    @patch.object(item_create_counter, "add", wraps=item_create_counter.add)
    def test_item_create_metric(self, mock_add: MagicMock):
        ItemFactory.create()
        mock_add.assert_called_once_with(1)

    @patch.object(item_update_counter, "add", wraps=item_update_counter.add)
    def test_item_update_metric(self, mock_add: MagicMock):
        item = ItemFactory.create()
        item.naam = "Updated"
        item.save()
        mock_add.assert_called_once_with(1)

    @patch.object(item_delete_counter, "add", wraps=item_delete_counter.add)
    def test_item_delete_metric(self, mock_add: MagicMock):
        item = ItemFactory.create()
        item.delete()
        mock_add.assert_called_once_with(1)
