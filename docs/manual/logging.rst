.. _manual_logging:

Logging
=======

Format
------

Referentielijsten emits structured logs (using `structlog <https://www.structlog.org/en/stable/>`_).
A log line can be formatted like this:

.. code-block:: json

    {
        "id": "1",
        "code": "ABC-1",
        "naam": "Tabel 1",
        "event": "tabel_created",
        "user_id": null,
        "request_id": "2f9e9a5b-d549-4faa-a411-594aa8a52eee",
        "timestamp": "2025-05-19T14:09:20.339166Z",
        "logger": "referentielijsten.api.signals",
        "level": "info"
    }

Each log line will contain an ``event`` type, a ``timestamp`` and a ``level``.
Dependent on your configured ``LOG_LEVEL`` (see :ref:`installation_env_config` for more information),
only log lines with of that level or higher will be emitted.

Referentielijsten log events
----------------------------

Below is the list of logging ``event`` types that referentielijsten can emit. In addition to the mentioned
context variables, these events will also have the **request bound metadata** described in the :ref:`django-structlog documentation <request_events>`.

API
~~~

* ``tabel_created``: created an ``Tabel`` via the API. Additional context: ``id``, ``code``, ``naam``.
* ``tabel_updated``: updated an ``Tabel`` via the API. Additional context: ``id``, ``code``, ``naam``.
* ``item_created``: created an ``Item`` via the API. Additional context: ``id``, ``code``, ``naam``.
* ``item_updated``: updated an ``Item`` via the API. Additional context: ``id``, ``code``, ``naam``..

Third party library events
--------------------------

For more information about log events emitted by third party libraries, refer to the documentation
for that particular library

* :ref:`Django (via django-structlog) <request_events>`
