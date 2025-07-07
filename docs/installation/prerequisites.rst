.. _installation_prerequisites:

Prerequisites
=============

Referentielijsten is most often deployed as a Docker container. While the
`container images <https://hub.docker.com/r/maykinmedia/referentielijsten-api/>`_ contain all the
necessary dependencies, Referentielijsten does require extra service to deploy the full stack.
These dependencies and their supported versions are documented here.

The ``docker-compose.yml`` (not suitable for production usage!) in the root of the
repository also describes these dependencies.

PostgreSQL
----------

.. warning::

   Since Referentielijsten version 0.4.0, PostgreSQL version 14 or higher is required. Attempting
   to deploy this version of Referentielijsten with PostgreSQL 13 or lower will result in errors!

Referentielijsten currently only supports PostgreSQL as datastore.

The supported versions in the table below are tested in the CI pipeline.

================ =========== ======= ======= ======= =======
Postgres version 13 or lower 14      15      16      17
================ =========== ======= ======= ======= =======
Supported?       |cross|     |check| |check| |check| |check|
================ =========== ======= ======= ======= =======

.. warning:: Referentielijsten only supports maintained versions of PostgreSQL. Once a version is
   `EOL <https://www.postgresql.org/support/versioning/>`_, support will
   be dropped in the next release.

Redis
-----

Referentielijsten uses Redis as a cache backend, especially relevant for admin sessions.

Supported versions: 5, 6, 7.

.. |check| unicode:: U+2705 .. ✅
.. |cross| unicode:: U+274C .. ❌
