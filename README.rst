=====================
Referentielijsten API
=====================

:Version: 0.7.1
:Source: https://github.com/maykinmedia/referentielijsten
:Keywords: referentielijsten, stamtabellen

|docs| |docker|

De Referentielijsten API is een generieke API voor eenvoudige herbruikebare
lijsten (`English version`_)

Ontwikkeld en gefinancierd door `Maykin B.V.`_.


Introductie
===========

Er zijn op dit moment 3 initiatieven voor referentielijsten. In de VNG API
standaard voor Zaakgericht Werken is een variant aanwezig die nooit is
geformaliseerd. In het VNG initiatief voor een Klantinteracties API is ook een
variant die net even afwijkt en ook niet formeel is vastgesteld. Ten slotte is
er nog de Objecten API, die voor dit doel soms gebruikt wordt. Deze kan echter
geen uniekheid afdwingen van items in de lijst en bevat teveel vrijheid in de
attributen.

Vandaar dat er is gekozen voor een generieke aanpak voor referentielijsten, die
zijn eigen API verdient. De API is bedoeld als registratie van herbruikbare
lijsten waarbij de waarden van deze lijsten mag worden opgeslagen in andere
registraties. Dit voorkomt onnodige calls naar deze API voor enkel een
tekstuele waarde.


API specificatie
================

|lint-oas| |generate-sdks| |generate-postman-collection|

==============  ==============  =============================
Versie          Release datum   API specificatie
==============  ==============  =============================
latest          n/a             `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/src/referentielijsten/api/openapi.yaml>`_,
                                (`verschillen <https://github.com/maykinmedia/referentielijsten/compare/0.7.1..master>`_)
0.7.1           2026-02-05      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.7.1/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.7.1/src/referentielijsten/api/openapi.yaml>`_
0.7.0           2025-12-01      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.7.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.7.0/src/referentielijsten/api/openapi.yaml>`_
0.6.0           2025-10-03      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.6.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.6.0/src/referentielijsten/api/openapi.yaml>`_
0.5.1           2025-09-23      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.5.1/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.5.1/src/referentielijsten/api/openapi.yaml>`_
0.5.0           2025-07-10      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.5.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.5.0/src/referentielijsten/api/openapi.yaml>`_
0.4.0           2025-05-28      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.4.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.4.0/src/referentielijsten/api/openapi.yaml>`_
0.3.2           2025-05-13      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.3.2/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.3.2/src/referentielijsten/api/openapi.yaml>`_
0.3.1           2025-04-11      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.3.1/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.3.1/src/referentielijsten/api/openapi.yaml>`_
0.3.0           2025-03-04      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.3.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.3.0/src/referentielijsten/api/openapi.yaml>`_
0.2.0           2024-10-04      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.2.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.2.0/src/referentielijsten/api/openapi.yaml>`_
0.1.0           2024-05-28      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.1.0/src/referentielijsten/api/openapi.yaml>`_,
                                `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/maykinmedia/referentielijsten/0.1.0/src/referentielijsten/api/openapi.yaml>`_
==============  ==============  =============================

Vorige versies worden nog 6 maanden ondersteund nadat de volgende versie is
uitgebracht.

Zie: `Alle versies en wijzigingen <https://github.com/maykinmedia/referentielijsten/blob/master/CHANGELOG.rst>`_


Ontwikkelaars
=============

|build-status| |coverage| |code-style| |codeql| |ruff| |python-versions|

Deze repository bevat de broncode voor Referentielijsten API. Om snel aan de slag
te gaan, raden we aan om de Docker image te gebruiken. Uiteraard kan je ook
het project zelf bouwen van de broncode. Zie hiervoor
`INSTALL.rst <INSTALL.rst>`_.

Quickstart
----------

1. Download en start Referentielijsten API:

   .. code:: bash

      $ wget https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/docker-compose.yml
      $ docker-compose up -d --no-build
      $ docker-compose exec web src/manage.py createsuperuser

2. In de browser, navigeer naar ``http://localhost:8000/`` om de beheerinterface
   en de API te benaderen.


Links
=====

* `Documentatie <https://referentielijsten-api.readthedocs.io/en/latest/>`_
* `Docker image <https://hub.docker.com/r/maykinmedia/referentielijsten-api>`_
* `Issues <https://github.com/maykinmedia/referentielijsten/issues>`_
* `Code <https://github.com/maykinmedia/referentielijsten>`_


Licentie
========

Copyright © Maykin 2024

Licensed under the EUPL_


.. _`English version`: README.EN.rst

.. _`Maykin B.V.`: https://www.maykinmedia.nl

.. _`EUPL`: LICENSE.md

.. |build-status| image:: https://github.com/maykinmedia/referentielijsten/actions/workflows/ci.yml/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/referentielijsten/actions/workflows/ci.yml

.. |docs| image:: https://readthedocs.org/projects/referentielijsten-api/badge/?version=latest
    :target: https://referentielijsten-api.readthedocs.io/
    :alt: Documentation Status

.. |coverage| image:: https://codecov.io/github/maykinmedia/referentielijsten/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/maykinmedia/referentielijsten

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. |code-style| image:: https://github.com/maykinmedia/referentielijsten/actions/workflows/code-quality.yml/badge.svg?branch=master
    :alt: Code style
    :target: https://github.com/maykinmedia/referentielijsten/actions/workflows/code-quality.yml

.. |codeql| image:: https://github.com/maykinmedia/referentielijsten/actions/workflows/codeql-analysis.yml/badge.svg?branch=master
    :alt: CodeQL scan
    :target: https://github.com/maykinmedia/referentielijsten/actions/workflows/codeql-analysis.yml

.. |docker| image:: https://img.shields.io/docker/v/maykinmedia/referentielijsten-api.svg?sort=semver
    :alt: Docker image
    :target: https://hub.docker.com/r/maykinmedia/referentielijsten-api

.. |python-versions| image:: https://img.shields.io/badge/python-3.12%2B-blue.svg
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
