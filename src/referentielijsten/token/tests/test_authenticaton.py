from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.tests import reverse

from referentielijsten.api.models import Tabel
from referentielijsten.api.tests.factories import TabelFactory


class TestCrudCallsWithoutAuthorization(APITestCase):
    def test_list(self):
        list_url = reverse(Tabel)
        TabelFactory.create_batch(2)

        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
