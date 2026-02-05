==============
Change history
==============

0.7.1 (2026-02-05)
------------------

**Documentation**

* [:open-api-framework:`197`] Update OpenAPI specification:

    * Add documentation for the ``pageSize`` parameter including maximum value (500).
    * Use ``DynamicPageSizePagination`` as the default pagination class.

**Project maintenance**

* Avoid using ``event`` key in uwsgi logs
* Upgrade dependencies

    * ``django`` to 5.2.11
    * ``commonground-api-common`` to 2.10.7
    * ``urllib3`` to 2.6.3
    * ``cbor2`` to 5.8.0
    * ``protobuf`` to 6.33.5

0.7.0 (2025-12-01)
------------------

.. warning::

    Changes to format of ``setup_configuration`` data for OpenID connect

    In this release, ``mozilla-django-oidc-db`` has been updated to version 1.1.0, which requires the new data format.
    The old format is deprecated and will be removed in future releases.

    The new configuration must be used, as it splits the previous solo model configuration into ``OIDCProvider`` and ``OIDCClient``
    configurations, making it easier to re-use identity provider settings across multiple client IDs.

    Additionally, any configuration using ``django-setup-configuration`` must be updated to reflect these changes,
    as it is now split into two distinct sections: one for ``providers`` and one for ``clients``.
    This separation also exists in the admin interface, so both sections can be configured directly through the user interface.
    For example:

    .. code-block:: yaml

        providers:
          - identifier: example-provider
            # other provider settings
        clients:
          - identifier: admin-oidc
            oidc_provider_identifier: example-provider
            # other client settings

    For detailed configuration, see :ref:`Admin OIDC Configuration Step  <ref_step_mozilla_django_oidc_db.setup_configuration.steps.AdminOIDCConfigurationStep>`.
    Make sure to check which fields are marked as ``DEPRECATED`` and replace them with the fields that are mentioned as replacements.

**New features**

* [:open-api-framework:`188`] Add data dump script (see :ref:`scripts` for more information)
* [:open-api-framework:`152`] Add OpenTelemetry (``OTel``) for collecting and exporting application metrics.

    * Metrics now exposed include:

        - HTTP request durations.
        - Number of active requests.
        - Number of users, logins, logouts, failed logins, and account lockouts.
        - **CRUD** operations for the following endpoints:

          - ``/tabel``
          - ``/item``

    * All metrics are exported using the **OpenTelemetry standard**, enabling seamless integration with existing monitoring and visualization platforms.

.. note::

    The OpenTelemetry SDK is **enabled by default**.

    If you do not have an endpoint to send system telemetry to, update your deployment to **disable it** by setting the environment variable:

    .. code-block:: bash

        OTEL_SDK_DISABLED=true

    If this is not done, warnings will be emitted to the container logs. The application will continue to function normally.

    All available metrics and details can be found in the :ref:`Observability documentation <installation_observability_index>`.

**Project maintenance**

* Upgrade dependencies

    * django to 5.2.8
    * pip to 25.3
    * open-api-framework to 0.13.2
    * commonground-api-common to 2.10.5
    * django-setup-configuration to 0.11.0
    * mozilla-django-oidc-db to 1.1.0

* [:open-api-workflows:`31`] Upgrade workflows to v6
* [:open-api-framework:`191`] upgrade nodejs to v24
* [:open-api-framework:`163`] Integrate ``maykin-common``

**Bugfixes**

* [:commonground-api-common:`134`] Ensure API errors are sent to Sentry

0.6.0 (2025-10-06)
------------------

**New features**

* [:open-api-framework:`175`] Changes to logging of handled and unhandled exceptions
  (see :ref:`manual_logging_exceptions` for more information)

    * Log events for handled API exceptions (e.g. HTTP 400) now include ``invalid_params``
    * Log events for unhandled API exceptions (e.g. HTTP 500) now include the traceback via ``exception``

* [:open-api-framework:`184`] ``setup_configuration`` now supports pulling values from
  environment variables in YAML configuration by using ``value_from`` (see `setup_configuration documentation`_ for more information)

.. TODO should be reference to readthedocs
.. _setup_configuration documentation: https://github.com/maykinmedia/django-setup-configuration/blob/main/README.rst#environment-variable-substitution

**Project maintenance**

* Upgrade dependencies

    * Django to 5.2.7
    * django-csp to 4.0
    * open-api-framework to 0.13.1
    * zgw-consumers to 1.0.0
    * django-privates to 3.1.1
    * commonground-api-common to 2.10.1


0.5.1 (2025-09-23)
------------------

.. warning::
     The default number of ``UWSGI_THREADS`` has been changed to 4.

**Project maintenance**

* [:open-api-framework:`85`] Set UWSGI_THREADS to 4 for improved concurrency.

* Upgrade dependencies

    * open-api-framework to 0.12.0
    * zgw-consumers to 1.0.0
    * django-privates to 3.1.1
    * commonground-api-common to 2.9.0

**Documentation**

* [:open-api-framework:`159`] Add model image docs creation (see :ref:`uml_diagrams`).


0.5.0 (2025-07-10)
------------------

.. warning::

    The logging format has been changed from unstructured to structured with `structlog <https://www.structlog.org/en/stable/>`_.
    For more information on the available log events and their context, see :ref:`manual_logging`.

**New features**

    * [:referentielijsten:`88`] Add structlog for observability

**Project maintenance**

    * [:open-api-framework:`139`] Integrate django-upgrade-check for easier Django upgrades and compatibility.
    * [:open-api-framework:`151`] Configure pyproject.toml, moving ruff and bump-my-version configs for cleaner setup.

* Upgrade dependencies

    * Django to 5.2.3
    * open-api-framework to 0.11.0
    * requests to 2.32.4
    * urllib3 to 2.5.0
    * uwsgi to 2.0.26
    * vcrpy to 7.0.0

**Bugfixes**

* [:referentielijsten:`89`] Fix dark/light theme in the Django Admin interface.


0.4.0 (2025-05-28)
------------------

.. warning::

    This release upgrades Django to version 5.2.1, which requires PostgreSQL version 14 or higher.
    Attempting to deploy with PostgreSQL <14 will cause errors during deployment.

**New features**

* [:referentielijsten:`70`] Simplified CSV/Excel import with table selection and optional fields
* [:referentielijsten:`72`] Add link to related items in Admin List View

**Project maintenance**

* Upgrade dependencies

  * [:open-api-framework:`140`] Python to 3.12
  * [:referentielijsten:`82`] Django to 5.2.1
  * tornado to 6.5.1
  * open-api-framework to 0.10.1
  * commonground-api-common to 2.6.4
  * setuptools to 80.8.0

* Replace OAS GitHub actions workflows with single workflow
* [:open-api-framework:`132`] Remove ``pytest`` and ``check_sphinx.py``, replace with simpler commands
* [:open-api-framework:`133`] Replace ``black``, ``isort`` and ``flake8`` with ``ruff`` and update code-quality workflow

**Bugfixes**

* Do not use ``save_outgoing_requests`` log handler if ``LOG_REQUESTS`` is set to false


0.3.2 (2025-05-13)
------------------

**Project maintenance**

* Upgrade Python dependencies

  * ``jinja2`` to 3.1.6
  * ``httpcore`` to 1.0.9
  * ``h11`` to 0.16.0

* Upgrade npm packages to fix vulnerabilities


0.3.1 (2025-04-11)
------------------

**Bugfixes**

* [:referentielijsten:`55`] Load fixtures automatically in docker

**Project maintenance**

* [:open-api-framework:`117`] Confirm support for Postgres 17
* [:open-api-framework:`117`] Upgrade nodejs version in CI pipeline to 20
* [:open-api-framework:`117`] Upgrade development dependencies

  * Development tools: black to 25.1.0, flake to 7.1.2 and isort to 6.0.1

* Upgrade dependencies

  * ``open-api-framework`` to 0.9.6
  * ``django`` to 4.2.20
  * ``cryptography`` to 44.0.1
  * ``jinja2`` to 3.1.5
  * ``commonground-api-common`` to 2.5.5
  * ``notifications-api-common`` to 0.7.1
  * ``django-setup-configuration`` to 0.7.2

* Remove tj-actions/changed-files action from CI and replace it with a script
* [:open-api-framework:`115`] Ensure OAS check always runs in CI

0.3.0 (2025-03-04)
------------------

**New features**

* [:open-api-framework:`23`] Add support for new version of ``django-setup-configuration``, the following steps were
  added/updated. For more information on how to provide configuration for these steps, see
  :ref:`installation_configuration_cli`

    * Configuration of OpenID Connect authentication for admin users (Single Sign On)


**Bugfixes and QOL**

* [:referentielijsten:`41`] Order API endpoints by pk (descending)
* [:open-api-framework:`79`] disable admin nav sidebar


**Documentation**

* [:referentielijsten:`43`] Update documentation for setup-configuration
* Add configuration for readthedocs

**Project maintenance**

* Upgrading dependencies:

   * Upgrade npm packages to fix vulnerabilities
   * Upgrade python packages to fix vulnerabilities
   * Upgrade open-api-framework to 0.9.3
   * Upgrade mozilla-django-oidc-db to 0.22.0
   * Upgrade django-setup-configuration to 0.7.1
   * Upgrade zgw-consumers to 0.35.1
   * Upgrade commonground-api-common to 2.5.1
* [:open-api-framework:`107`] Add bump-my-version to dev dependencies
* [:open-api-framework:`102`] Add quick-start workflow to test docker-compose.yml
* [:open-api-framework:`44`] add workflow to CI to auto-update open-api-framework
* [:open-api-framework:`81`] Switch from pip-compile to UV
* [:open-api-framework:`92`] Fix docker latest tag publish
* [:open-api-framework:`13`] Switch to use reusable open-api-workflows in github actions

0.2.0 (2024-10-04)
------------------

**New features**

* [#31] Updated open-api-framework to 0.8.1, which includes adding CSRF, CSP and HSTS settings (#438).
  All new environment variables are added to the `documentation <https://referentielijsten-api.readthedocs.io/en/latest/installation/config.html>`_
* [#15] Add import export to item admin
* [#7] Add OIDC login

.. warning::

    ``SECURE_HSTS_SECONDS`` has been added with a default of 31536000 seconds, ensure that
    before upgrading to this version of open-api-framework, your entire application is served
    over HTTPS, otherwise this setting can break parts of your application (see https://docs.djangoproject.com/en/4.2/ref/middleware/#http-strict-transport-security)

.. warning::

   Deployment tooling updates required - additional containers needed.

   Redis is now required as a cache backend, make sure to add and configure a Redis container

.. warning::

   Two factor authentication was added (by default it is enabled, to disable it, set the ``DISABLE_2FA`` envvar to ``True``

**Bugfixes and QOL**

* [#29] Fixed npm vulnerabilities
* [#21] Add missing pyquery dependency
* [#18] Fix help-text icon layout in the admin

**Documentation**

* [#19] Document env vars

**Project maintenance**

* [#28] Update pip in stage 3 of dockerfile
* [#27] Moved setuptools installation in dockerfile
* [#26] Update open-api-framework
* [#25] Update setup tools
* [#24] Upgrade webob
* [#23] Upgrade django version
* [#22] Add keycloak docker
* [#20] Update dependencies and fixed broken oidc tests
* [#17] Refactor base settings

0.1.0 (2024-05-28)
------------------


* Initial release.
