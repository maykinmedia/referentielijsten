from django.test import override_settings

from freezegun import freeze_time
from rest_framework import status
from vng_api_common.tests import reverse

from referentielijsten.token.tests.api_testcase import APITestCase

from ..models import Tabel
from .factories import TabelFactory


@override_settings(USE_TZ=False)
class TabellenApiTests(APITestCase):
    def test_tabellen_with_no_query_params(self):
        url = reverse(Tabel)
        TabelFactory.create_batch(3)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["count"], 3)

    def test_tabellen_with_code(self):
        url = reverse(Tabel)
        TabelFactory.create(code="123", naam="first tabel")
        TabelFactory.create(code="456", naam="second tabel")
        TabelFactory.create(code="789", naam="third tabel")

        response = self.client.get(url, {"code": "456"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()["results"]

        self.assertEqual(response_data[0]["code"], "456")
        self.assertEqual(response_data[0]["naam"], "second tabel")

        response = self.client.get(url, {"code": "123456789"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 0)

    @freeze_time("2024-01-01 00:00:00")
    def test_tabellen_is_geldig(self):
        url = reverse(Tabel)
        TabelFactory.create(
            code="1", naam="geldig", einddatum_geldigheid="2025-01-01 00:00:00"
        )
        TabelFactory.create(
            code="2", naam="ongeldig", einddatum_geldigheid="2023-01-01 00:00:00"
        )

        response = self.client.get(url, {"isGeldig": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 1)
        self.assertEqual(response_data["results"][0]["code"], "1")
        self.assertEqual(response_data["results"][0]["naam"], "geldig")

    @freeze_time("2024-01-01 00:00:00")
    def test_tabellen_is_not_geldig(self):
        url = reverse(Tabel)
        TabelFactory.create(
            code="1", naam="geldig", einddatum_geldigheid="2025-01-01 00:00:00"
        )
        TabelFactory.create(
            code="2", naam="ongeldig", einddatum_geldigheid="2023-01-01 00:00:00"
        )

        response = self.client.get(url, {"isGeldig": "false"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 1)
        self.assertEqual(response_data["results"][0]["code"], "2")
        self.assertEqual(response_data["results"][0]["naam"], "ongeldig")
