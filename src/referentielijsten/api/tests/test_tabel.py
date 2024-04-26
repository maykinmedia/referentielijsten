from django.test import override_settings

from freezegun import freeze_time
from rest_framework import status
from vng_api_common.tests import reverse

from referentielijsten.token.tests.api_testcase import APITestCase
from ..models import Tabel
from .factories import ItemFactory, TabelFactory


@override_settings(USE_TZ=False)
class TabelApiTests(APITestCase):
    def test_list_tabel_with_no_query_params(self):
        url = reverse(Tabel)
        TabelFactory.create_batch(3)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(len(response_data), 0)

    def test_list_tabel_with_code(self):
        url = reverse(Tabel)
        tabel1, *_ = TabelFactory.create_batch(3)
        item1, item2 = ItemFactory.create_batch(2, tabel=tabel1)

        response = self.client.get(url, {"code": tabel1.code})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data[0]["code"], tabel1.code)
        self.assertEqual(response_data[0]["naam"], tabel1.naam)
        self.assertEqual(response_data[0]["items"][0]["code"], item1.code)
        self.assertEqual(response_data[0]["items"][0]["naam"], item1.naam)
        self.assertEqual(response_data[0]["items"][1]["code"], item2.code)
        self.assertEqual(response_data[0]["items"][1]["naam"], item2.naam)

        response = self.client.get(url, {"code": "99999999999999999999999999"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(len(response_data), 0)

    def test_list_tabel_with_code_and_geldig(self):
        url = reverse(Tabel)
        tabel1, tabel2, _ = TabelFactory.create_batch(3)
        item1, item2 = ItemFactory.create_batch(2, tabel=tabel1)
        ItemFactory.create_batch(2, tabel=tabel2)

        response = self.client.get(url, {"code": tabel1.code, "geldig": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data[0]["code"], tabel1.code)
        self.assertEqual(response_data[0]["naam"], tabel1.naam)
        self.assertEqual(response_data[0]["items"][0]["code"], item1.code)
        self.assertEqual(response_data[0]["items"][0]["naam"], item1.naam)
        self.assertEqual(response_data[0]["items"][1]["code"], item2.code)
        self.assertEqual(response_data[0]["items"][1]["naam"], item2.naam)

        response = self.client.get(url, {"code": tabel1.code, "geldig": "false"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(len(response_data), 0)

    @freeze_time("2024-01-01 00:00:00")
    def test_list_tabel_not_geldig(self):
        url = reverse(Tabel)
        tabel1 = TabelFactory.create(einddatum_geldigheid="2023-01-01 00:00:00")

        response = self.client.get(url, {"code": tabel1.code, "geldig": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(len(response_data), 0)

    @freeze_time("2024-01-01 00:00:00")
    def test_list_tabel_with_items_that_are_not_geldig(self):
        url = reverse(Tabel)
        tabel1 = TabelFactory.create()
        item1 = ItemFactory.create(tabel=tabel1)
        ItemFactory.create(tabel=tabel1, einddatum_geldigheid="2023-01-01 00:00:00")
        ItemFactory.create(tabel=tabel1, begindatum_geldigheid="2025-01-01 00:00:00")

        response = self.client.get(url, {"code": tabel1.code, "geldig": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data[0]["code"], tabel1.code)
        self.assertEqual(response_data[0]["naam"], tabel1.naam)
        self.assertEqual(len(response_data[0]["items"]), 1)
        self.assertEqual(response_data[0]["items"][0]["code"], item1.code)
        self.assertEqual(response_data[0]["items"][0]["naam"], item1.naam)
