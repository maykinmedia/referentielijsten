from opentelemetry import metrics

meter = metrics.get_meter("referentielijsten.api")

tabel_create_counter = meter.create_counter(
    "referentielijsten.api.table.creates",
    description="Amount of zaken created.",
    unit="1",
)
tabel_update_counter = meter.create_counter(
    "referentielijsten.api.table.updates",
    description="Amount of zaken updated.",
    unit="1",
)
tabel_delete_counter = meter.create_counter(
    "referentielijsten.api.table.deletes",
    description="Amount of zaken deleted.",
    unit="1",
)

item_create_counter = meter.create_counter(
    "referentielijsten.api.item.creates",
    description="Amount of zaken created.",
    unit="1",
)
item_update_counter = meter.create_counter(
    "referentielijsten.api.item.updates",
    description="Amount of zaken updated.",
    unit="1",
)
item_delete_counter = meter.create_counter(
    "referentielijsten.api.item.deletes",
    description="Amount of zaken deleted.",
    unit="1",
)
