from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from import_export.formats.base_formats import CSV

from ..admin import ItemAdmin, ItemResource, admin
from ..forms import ItemImportForm
from ..models import Item
from .factories import TabelFactory


class ItemAdminTests(TestCase):
    def get_test_form(self, form_data):
        dummy_file = SimpleUploadedFile("test.csv", b"code,naam\n123,Test Item\n")
        dummy_file.tmp_storage_name = "test.csv"

        form_data["format"] = "0"
        form = ItemImportForm(
            [CSV],
            [ItemResource],
            data=form_data,
            files={"import_file": dummy_file},
        )
        return form

    def test_get_confirm_form_initial(self):
        tabel = TabelFactory.create(code="123")
        form = self.get_test_form({"selected_tabel": tabel.pk})
        self.assertTrue(form.is_valid(), form.errors)

        item_admin = ItemAdmin(Item, admin.site)
        initial_data = item_admin.get_confirm_form_initial(self.client, form)

        self.assertEqual(initial_data["selected_tabel"], tabel)

    def test_get_import_resource_kwargs(self):
        tabel = TabelFactory.create(code="123")

        form = self.get_test_form({"selected_tabel": tabel.pk})
        self.assertTrue(form.is_valid(), form.errors)

        item_admin = ItemAdmin(Item, admin.site)
        resource_kwargs = item_admin.get_import_resource_kwargs(self.client, form=form)

        self.assertEqual(resource_kwargs["selected_tabel"], tabel)

    def test_before_import_row_sets_tabel_id(self):
        tabel = TabelFactory.create(code="123")

        resource = ItemResource(selected_tabel=tabel)
        row = {"code": "123", "naam": "Test Item"}

        resource.before_import_row(row)

        self.assertEqual(row["tabel"], tabel.id)
