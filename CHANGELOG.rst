==============
Change history
==============

0.2.0
=====

*?? ??, 2024*

**New features**

* updated open-api-framework to 0.8.0, which includes adding CSRF, CSP and HSTS settings (#438).
  All new environment variables are added to the `documentation <https://objects-and-objecttypes-api.readthedocs.io/en/latest/installation/config.html>`_

.. warning::

    ``SECURE_HSTS_SECONDS`` has been added with a default of 31536000 seconds, ensure that
    before upgrading to this version of open-api-framework, your entire application is served
    over HTTPS, otherwise this setting can break parts of your application (see https://docs.djangoproject.com/en/4.2/ref/middleware/#http-strict-transport-security)


.. warning::

   Deployment tooling updates required - additional containers needed.

   Redis is now required as a cache backend, make sure to add and configure a Redis container

.. warning::

   Two factor authentication was added (by default it is enabled, to disable it, set the ``DISABLE_2FA`` envvar to ``True``)

0.1.0
=====

*May 28, 2024*

* Initial release.
