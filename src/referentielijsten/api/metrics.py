from opentelemetry import metrics

meter = metrics.get_meter("referentielijsten.api")

tabel_create_counter = meter.create_counter(
    "referentielijsten.tabel.creates",
    description="Amount of tabels created.",
    unit="1",
)
tabel_update_counter = meter.create_counter(
    "referentielijsten.tabel.updates",
    description="Amount of tabels updated.",
    unit="1",
)
tabel_delete_counter = meter.create_counter(
    "referentielijsten.tabel.deletes",
    description="Amount of tabels deleted.",
    unit="1",
)

item_create_counter = meter.create_counter(
    "referentielijsten.item.creates",
    description="Amount of items created.",
    unit="1",
)
item_update_counter = meter.create_counter(
    "referentielijsten.item.updates",
    description="Amount of items updated.",
    unit="1",
)
item_delete_counter = meter.create_counter(
    "referentielijsten.item.deletes",
    description="Amount of items deleted.",
    unit="1",
)
