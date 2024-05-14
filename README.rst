==================
referentielijsten
==================

:Version: 0.1.0
:Source: https://github.com/maykinmedia/referentielijsten
:Keywords: referentielijsten, stambomen
:PythonVersion: 3.11

|docker|

``<oneliner describing the project>``

Developed by `Maykin Media B.V.`_


Introduction
============

``<describe the project in a few paragraphs and briefly mention the features>``

API specificatie
================

Hieronder staat de versie van Open Klant en welke versie van de 
API-specificatie wordt aangeboden.

==========================  ==============  =============   ================
Referentielijsten versie    API versie      Release datum   API specificatie
==========================  ==============  =============   ================
master/latest               n/a             n/a             `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/src/api/openapi.yaml>`_,
                                                            `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/src/api/openapi.yaml>`_


Ready-to-go implementatie
=========================

|build-status| |coverage| |code-style| |codeql| |black| |python-versions|

Deze implementatie is bedoeld als referentie implementatie van de API
specificaties maar tevens een productiewaardig component dat ingezet kan worden
in het ICT landschap van de overheid.

Quickstart
----------

1. Download en start Open Klant:

   .. code:: bash

      $ wget https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/docker-compose.yml
      $ docker-compose up -d --no-build
      $ docker-compose exec web src/manage.py createsuperuser

2. In de browser, navigeer naar ``http://localhost:8000/`` om de beheerinterface
   en de API te benaderen.


Links
=====

* `Docker image <https://hub.docker.com/r/maykinmedia/referentielijsten>`_
* `Issues <https://github.com/maykinmedia/referentielijsten/issues>`_
* `Code <https://github.com/maykinmedia/referentielijsten>`_
* `Community <https://commonground.nl/groups/view/6bca7599-0f58-44e4-a405-7aa3a4c682f3/referentielijsten>`_


References
==========

* `Issues <https://taiga.maykinmedia.nl/project/referentielijsten>`_
* `Code <https://bitbucket.org/maykinmedia/referentielijsten>`_


.. _`Maykin B.V.`: https://www.maykinmedia.nl

.. |build-status| image:: https://github.com/maykinmedia/referentielijsten/workflows/ci.yml/badge.svg?branch=master
    :alt: Build status
    :target: https://github.com/maykinmedia/referentielijsten/actions?query=workflow%3Aci

.. |coverage| image:: https://codecov.io/github/maykinmedia/referentielijsten/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/maykinmedia/referentielijsten

.. |code-style| image:: https://github.com/maykinmedia/referentielijsten/actions/workflows/code-style.yml/badge.svg?branch=master
    :alt: Code style
    :target: https://github.com/maykinmedia/referentielijsten/actions/workflows/code-style.yml

.. |codeql| image:: https://github.com/maykinmedia/referentielijsten/actions/workflows/codeql.yml/badge.svg?branch=master
    :alt: CodeQL scan
    :target: https://github.com/maykinmedia/referentielijsten/actions/workflows/codeql.yml

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style
    :target: https://github.com/psf/black

.. |docker| image:: https://img.shields.io/docker/v/maykinmedia/referentielijsten?sort=semver
    :alt: Docker image
    :target: https://hub.docker.com/r/maykinmedia/referentielijsten

.. |python-versions| image:: https://img.shields.io/badge/python-3.11%2B-blue.svg
    :alt: Supported Python version

.. |lint-oas| image:: https://github.com/maykinmedia/referentielijsten/workflows/actions/lint-oas/badge.svg
    :alt: Lint OAS
    :target: https://github.com/maykinmedia/referentielijsten/actions?query=workflow%3Alint-oas
