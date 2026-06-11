.. _installation_quickstart:

Quickstart
==========

A simple ``docker-compose.yml`` file is available to get the APIs
up and running in minutes. This file has some convenience settings to get
started quickly and these should never be used for anything besides testing:

* A default secret is set in the ``SECRET_KEY`` environment variable.
* A predefined database and database account is used.
* API authorizations are disabled.

With the above remarks in mind, let's go:

Referentielijsten
-----------------

1. Create a project folder:

   .. code:: shell

      $ mkdir referentielijsten
      $ cd referentielijsten

2. Download the ``docker-compose`` file:

   .. tabs::

      .. tab:: Linux

         .. code:: shell

            $ wget https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/docker-compose.yml

      .. tab:: Windows Powershell 3

         .. code:: shell

            PS> wget https://raw.githubusercontent.com/maykinmedia/referentielijsten/master/docker-compose.yml

3. Start the Docker containers:

   .. code:: shell

      $ docker compose -f docker-compose-qs.yml up -d --no-build


5. Create a superuser

   .. code:: shell

      $ docker compose exec web src/manage.py createsuperuser
