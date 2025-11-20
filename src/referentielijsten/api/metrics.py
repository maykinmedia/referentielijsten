from opentelemetry import metrics

meter = metrics.get_meter("referentielijsten.api")

tabel_create_counter = meter.create_counter(
    "referentielijsten.api.tabel.creates",
    description="Amount of zaken created.",
    unit="1",
)
tabel_update_counter = meter.create_counter(
    "referentielijsten.api.tabel.updates",
    description="Amount of zaken updated.",
    unit="1",
)
tabel_delete_counter = meter.create_counter(
    "referentielijsten.api.tabtabelle.deletes",
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
