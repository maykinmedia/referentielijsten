==============
Change history
==============

0.2.0
=====

*October 04, 2024*

**New features**

* [#31] Updated open-api-framework to 0.8.1, which includes adding CSRF, CSP and HSTS settings (#438).
  All new environment variables are added to the `documentation <https://objects-and-objecttypes-api.readthedocs.io/en/latest/installation/config.html>`_
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

0.1.0
=====

*May 28, 2024*

* Initial release.
