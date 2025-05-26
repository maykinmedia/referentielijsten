from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django_webtest import WebTest
from maykin_2fa.test import disable_admin_mfa

from referentielijsten.accounts.tests.factories import UserFactory

from .factories import ItemFactory, TabelFactory


@disable_admin_mfa()
class TabellenAdminTests(WebTest):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.superuser = UserFactory.create(superuser=True)

    def test_items_link_returns_correct_admin_url(self):
        tabel = TabelFactory.create()

        # TODO replace with reverse(..., query=...) once Django is upgraded to 5.2
        expected_url = (
            reverse("admin:api_item_changelist") + f"?tabel__code={tabel.code}"
        )
        expected_html = (
            f'<a href="{expected_url}">{_("Show items in item list view")}</a>'
        )

        response = self.app.get(
            reverse("admin:api_tabel_changelist"), user=self.superuser
        )
        self.assertIn(expected_html, response.content.decode())

    def test_items_link_target_url_is_accessible(self):
        tabel = TabelFactory.create(code="matching")
        tabel1 = TabelFactory.create(code="not")

        item = ItemFactory.create(tabel=tabel)
        item1 = ItemFactory.create(tabel=tabel1)

        url = reverse("admin:api_item_changelist") + f"?tabel__code={tabel.code}"

        response = self.app.get(url, user=self.superuser)
        self.assertEqual(response.status_code, 200)

        matching_item_change_url = reverse("admin:api_item_change", args=[item.id])
        self.assertIn(matching_item_change_url, response.text)

        other_item_change_url = reverse("admin:api_item_change", args=[item1.id])
        self.assertNotIn(other_item_change_url, response.text)
