.. _deployment_kubernetes:

==========
Kubernetes
==========

Here you can find a reference implementation of the Referentielijsten deployment for
a Kubernetes cluster using `Helm`_.

The `Helm chart`_ installs Referentielijsten and is dependent on a PostgreSQL
database, installed using a `subchart`_.

.. warning:: The default settings are unsafe and should only be used for
   development purposes. Configure proper secrets, enable persistence, add
   certificates before using in production.


Installation
============

Install the Helm chart with following commands:

.. code:: shell

   helm repo add maykinmedia https://maykinmedia.github.io/charts/
   helm search repo maykinmedia
   helm install my-release maykinmedia/referentielijsten


Use Kubernetes CLI to monitor the status of deployment:

.. code:: shell

   kubectl get pods


.. _`Helm`: https://helm.sh/
.. _`subchart`: https://github.com/bitnami/charts/tree/master/bitnami/postgresql
.. _`Helm chart`: https://github.com/maykinmedia/charts/tree/main/charts/referentielijsten
