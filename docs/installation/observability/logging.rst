.. _installation_observability_logging:

=======
Logging
=======

Logging is the practice of emitting log messages that describe what is happening in the
system, or "events" in short. Log events can have varying degrees of severity, such as
``debug``, ``info``, ``warning``, ``error`` or even ``critical``. By default, Referentielijsten
emits logs with level ``info`` and higher.

A collection of log events with a correlation ID (like a request or trace ID) allow one
to reconstruct the chain of events that took place which lead to a particular outcome.

Referentielijsten emits structured logs in JSON format (unless explicitly configured otherwise),
which should make log aggregation and analysis easier.

We try to keep a consistent log message structure, where the following keys
are (usually) present:

``source``
    The component in the application stack that produced the log entry. Typical
    values are ``uwsgi`` and ``app``.

``level``
    The severity level of the log message. One of ``debug``, ``info``, ``warning``,
    ``error`` or ``critical``.

``timestamp``
    The moment when the log entry was produced, a string in ISO-8601 format. Most of
    the logs have microsecond precision, but some of them are limited to second
    precision.

``event``
    The event that occurred, e.g. ``request_started`` or ``spawned worker (PID 123)``.
    This gives the semantic meaning to the log entry.

Other keys that frequently occur are:

``request_id``
    Present for application logs emitted during an HTTP request, makes it possible to
    correlate multiple log entries for a single request. Not available in logs emitted
    by background tasks or logs emitted before/after the Referentielijsten  app.

.. tip:: Certain log aggregation solutions require you to configure "labels" to extract
   for efficient querying. You can use the above summary of log context keys to configure
   this according to your needs.

.. note:: We can not 100% guarantee that every log message will always be JSON due to
   limitations in third party software/packages that we use. Most (if not all) log
   aggregation technologies support handling both structured and unstructured logs.


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
* ``tabel_deleted``: deleted an ``Tabel`` via the API. Additional context: ``id``, ``code``, ``naam``.
* ``item_created``: created an ``Item`` via the API. Additional context: ``id``, ``code``, ``naam``.
* ``item_updated``: updated an ``Item`` via the API. Additional context: ``id``, ``code``, ``naam``..
* ``item_deleted``: deleted an ``Item`` via the API. Additional context: ``id``, ``code``, ``naam``..

.. _manual_logging_exceptions:

Exceptions
----------

Handled exceptions follow a standardized JSON format to ensure consistency and improve error tracking.
Most fields are standard and include:
``title``, ``code``, ``status``, ``event``, ``source``, ``user_id``, ``request_id``, ``exception_id``, ``timestamp``, ``logger`` and ``level``.

A new field ``invalid_params`` has been added to provide detailed information about which input parameters caused the error in API calls.

    - ``name``: name of the invalid parameter
    - ``code``: specific error code
    - ``reason``: explanation/message of the error

.. code-block:: json

    {
        "title": "'Invalid input.'",
        "code": "invalid",
        "status": 400,
        "invalid_params": [
            {
            "name": "tabel__code",
            "code": "required",
            "reason": "Dit veld is vereist."
            }
        ],
        "event": "api.handled_exception",
        "user_id": null,
        "exception_id": "e0207775-bfc7-4ba6-b0f5-489e6e93030e",
        "request_id": "c75121fb-ac9f-474b-9ba9-ef7272add573",
        "timestamp": "2025-10-03T12:09:49.156009Z",
        "logger": "vng_api_common.exception_handling",
        "level": "error"
    }

Uncaught exceptions that occur via the API are logged as ``api.uncaught_exception`` events
and contain the traceback of the exception.

.. code-block:: json

    {
        "message": "division by zero",
        "event": "api.uncaught_exception",
        "user_id": null,
        "source": "app",
        "request_id": "b1c4db0e-da7f-4a9e-a9fe-efbb6420a907",
        "timestamp": "2025-10-03T12:09:04.238909Z",
        "logger": "vng_api_common.views",
        "level": "error",
        "exception": "Traceback (most recent call last):\n  File \"/usr/local/lib/python3.12/site-packages/rest_framework/views.py\", line 506, in dispatch\n    response = handler(request, *args, **kwargs)\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/app/src/referentielijsten/api/viewset.py\", line 63, in list\n    1 / 0\n    ~~^~~\nZeroDivisionError: division by zero"
    }

Third party library events
--------------------------

For more information about log events emitted by third party libraries, refer to the documentation
for that particular library

* :ref:`Django (via django-structlog) <request_events>`
