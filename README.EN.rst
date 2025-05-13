=====================
Referentielijsten API
=====================

:Version: 0.3.2
:Source: https://github.com/maykinmedia/referentielijsten
:Keywords: referentielijsten, stamtabellen

|docs| |docker|

The Referentielijsten API (Reference lists API) is a generic API for simple and
reusable data lists (`Nederlandse versie`_)

Developed and financed by `Maykin B.V.`_.


Introduction
=============

There are currently 3 initiatives for reference lists. In the VNG API standard 
for Zaakgericht Werken there is a variant that was never formalized. The VNG 
initiative for Klantinteracties API also includes a variant that differs 
slightly and has not been formally acknowledged. Finally, there is also the 
Objects API that is sometimes used for this purpose. However, it cannot enforce 
uniqueness of items in the list and offers too much freedom in attributes.

That is why a generic approach for reference lists was chosen, which
deserves its own API. The API is intended as a registration of reusable data 
lists where the values of these lists may be stored in others registrations. 
This prevents unnecessary calls to this API for just one textual value.


API specification
=================

|lint-oas| |generate-sdks| |generate-postman-collection|

==============  ==============  =============================
Version         Release date    API specification
==============  ==============  =============================
latest          n/a             `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/src/referentielijsten/api/openapi.yaml>`_,
                                (`diff <https://github.com/maykinmedia/referentielijsten/compare/0.1.0..master#diff-b9c28fec6c3f3fa5cff870d24601d6ab7027520f3b084cc767aefd258cb8c40a>`_)
0.1.0           2024-05-28      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.1.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.1.0/src/referentielijsten/api/openapi.yaml>`_
==============  ==============  =============================

Previous versions are supported for 6 month after the next version is released.

See: `All versions and changes <https://github.com/maykinmedia/referentielijsten/blob/master/CHANGELOG.rst>`_


Developers
==========

|build-status| |coverage| |black| |docker| |python-versions|

This repository contains the source code for Referentielijsten API. To quickly
get started, we recommend using the Docker image. You can also build the
project from the source code. For this, please look at 
`INSTALL.rst <INSTALL.rst>`_.

Quickstart
----------

1. Download and run Referentielijsten API:

   .. code:: bash

      $ wget https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/docker-compose.yml
      $ docker-compose up -d --no-build
      $ docker-compose exec web src/manage.py createsuperuser

2. In the browser, navigate to ``http://localhost:8000/`` to access the admin
   and the API.


References
==========

* `Documentation <https://TODO>`_
* `Docker image <https://hub.docker.com/r/maykinmedia/referentielijsten-api>`_
* `Issues <https://github.com/maykinmedia/referentielijsten/issues>`_
* `Code <https://github.com/maykinmedia/referentielijsten>`_
* `Community <https://TODO>`_


License
=======

Copyright © Maykin 2024

Licensed under the EUPL_


.. _`Nederlandse versie`: README.rst

.. _`Maykin B.V.`: https://www.maykinmedia.nl

.. _`EUPL`: LICENSE.md

.. |build-status| image:: https://github.com/maykinmedia/referentielijsten/actions/workflows/ci.yml/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/referentielijsten/actions/workflows/ci.yml

.. |docs| image:: https://readthedocs.org/projects/referentielijsten-and-objecttypes-api/badge/?version=latest
    :target: https://referentielijsten-and-objecttypes-api.readthedocs.io/
    :alt: Documentation Status

.. |coverage| image:: https://codecov.io/github/maykinmedia/referentielijsten/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/maykinmedia/referentielijsten

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style
    :target: https://github.com/psf/black

.. |docker| image:: https://img.shields.io/docker/v/maykinmedia/referentielijsten-api?sort=semver
    :alt: Docker image
    :target: https://hub.docker.com/r/maykinmedia/referentielijsten-api

.. |python-versions| image:: https://img.shields.io/badge/python-3.11%2B-blue.svg
    :alt: Supported Python version

.. |lint-oas| image:: https://github.com/maykinmedia/referentielijsten/workflows/lint-oas/badge.svg
    :alt: Lint OAS
    :target: https://github.com/maykinmedia/referentielijsten/actions?query=workflow%3Alint-oas

.. |generate-sdks| image:: https://github.com/maykinmedia/referentielijsten/workflows/generate-sdks/badge.svg
    :alt: Generate SDKs
    :target: https://github.com/maykinmedia/referentielijsten/actions?query=workflow%3Agenerate-sdks

.. |generate-postman-collection| image:: https://github.com/maykinmedia/referentielijsten/workflows/generate-postman-collection/badge.svg
    :alt: Generate Postman collection
    :target: https://github.com/maykinmedia/referentielijsten/actions?query=workflow%3Agenerate-postman-collection
