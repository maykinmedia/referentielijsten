from django.test import override_settings
from django.urls import reverse_lazy

from freezegun import freeze_time
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import ItemFactory, TabelFactory


@override_settings(USE_TZ=False)
class ItemsApiTests(APITestCase):
    url = reverse_lazy("item-list", kwargs={"version": 1})

    def test_items_with_no_tabel_code(self):
        ItemFactory.create_batch(3)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["invalidParams"],
            [
                {
                    "name": "tabel__code",
                    "code": "required",
                    "reason": "Dit veld is vereist.",
                }
            ],
        )

    def test_items_with_tabel_code(self):
        tabel = TabelFactory.create(code="123")
        item1, item2, item3 = ItemFactory.create_batch(3, tabel=tabel)

        tabel2 = TabelFactory.create(code="456")
        ItemFactory.create_batch(3, tabel=tabel2)

        response = self.client.get(self.url, {"tabel__code": "123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 3)
        results = response_data["results"]

        self.assertEqual(results[0]["code"], item3.code)
        self.assertEqual(results[1]["code"], item2.code)
        self.assertEqual(results[2]["code"], item1.code)

    def test_items_with_none_existing_tabel_code(self):
        TabelFactory.create(code="123")
        TabelFactory.create(code="456")
        TabelFactory.create(code="789")

        response = self.client.get(self.url, {"tabel__code": "123456789"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 0)

    @freeze_time("2024-01-01 00:00:00")
    def test_items_is_geldig(self):
        tabel = TabelFactory.create(code="123")
        ItemFactory(tabel=tabel, code="1", naam="geldig geen begindatum en einddatum")
        ItemFactory(
            tabel=tabel,
            code="2",
            naam="begindatum geldig",
            begindatum_geldigheid="2023-01-01 00:00:00",
        )
        ItemFactory(
            tabel=tabel,
            code="3",
            naam="einddatum geldig",
            einddatum_geldigheid="2025-01-01 00:00:00",
        )
        ItemFactory(
            tabel=tabel,
            code="4",
            naam="begindatum en einddatum geldig",
            begindatum_geldigheid="2023-01-01 00:00:00",
            einddatum_geldigheid="2025-01-01 00:00:00",
        )

        ItemFactory(
            tabel=tabel,
            code="5",
            naam="begindatum ongeldig",
            begindatum_geldigheid="2025-01-01 00:00:00",
        )
        ItemFactory(
            tabel=tabel,
            code="6",
            naam="einddatum ongeldig",
            einddatum_geldigheid="2023-01-01 00:00:00",
        )

        response = self.client.get(self.url, {"tabel__code": "123", "isGeldig": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 4)
        results = response_data["results"]

        self.assertEqual(results[0]["code"], "4")
        self.assertEqual(results[1]["code"], "3")
        self.assertEqual(results[2]["code"], "2")
        self.assertEqual(results[3]["code"], "1")

        response = self.client.get(
            self.url, {"tabel__code": "123", "isGeldig": "false"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data["count"], 2)
        results = response_data["results"]

        self.assertEqual(results[0]["code"], "6")
        self.assertEqual(results[1]["code"], "5")
