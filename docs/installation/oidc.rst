.. _manual_oidc:

===========================
OpenID Connect configureren
===========================

Referentielijsten ondersteunt Single Sign On (SSO) via het OpenID Connect protocol (OIDC) voor de beheerinterface.

Gebruikers kunnen op die manier inloggen op Referentielijsten met hun account bij de OpenID Connect provider. In deze
flow:

1. Klikt een gebruiker op het inlogscherm op *Inloggen met OIDC*
2. De gebruiker wordt naar de omgeving van de OpenID Connect provider geleid (bijv. Keycloak) waar ze inloggen met gebruikersnaam
   en wachtwoord (en eventuele Multi Factor Authentication)
3. De OIDC omgeving stuurt de gebruiker terug naar Referentielijsten (waar de account aangemaakt
   wordt indien die nog niet bestaat)
4. Een beheerder in Referentielijsten kent de juiste groepen toe aan deze gebruiker als deze
   voor het eerst inlogt.

.. note:: Standaard krijgen deze gebruikers **geen** toegang tot de beheerinterface. Deze
   rechten moeten door een (andere) beheerder :ref:`ingesteld <manual_users>` worden. De
   account is wel aangemaakt.

Configureren van OIDC zelf
==========================

Contacteer de IAM beheerders in je organisatie om een *Client* aan te
maken in de omgeving van de OpenID Connect provider.

Voor de **Redirect URI** vul je ``https://referentielijsten.gemeente.nl/oidc/callback`` in,
waarbij je ``referentielijsten.gemeente.nl`` vervangt door het relevante domein.

Aan het eind van dit proces moet je de volgende gegevens hebben (on premise):

* Server adres, bijvoorbeeld ``login.gemeente.nl``
* Client ID, bijvoorbeeld ``a7d14516-8b20-418f-b34e-25f53c930948``
* Client secret, bijvoorbeeld ``97d663a9-3624-4930-90c7-2b90635bd990``


Configureren van OIDC in Referentielijsten
==========================================
Het configureren van OIDC in referentielijsten kan via :ref:`installation_configuration_cli`.


Providersreferentie
===================

ADFS (on premise)
-----------------

For on premise ADFS, the discovery URL usually has the form
``https://login.gemeente.nl/adfs/.well-known/openid-configuration``.

Azure AD
--------

Azure Active Directory is a cloud-hosted identity provider from Microsoft, part of Azure webservices.

To use AAD as OIDC provider, you require a Tenant ID, usually in the same of a UUID v4.
This tenant ID is used in the discovery URL, having the form
``https://login.microsoftonline.com/${tenantId}/v2.0``.

Keycloak
--------

Keycloak is a multi-tenant IDP which itself can configure other IDPs.

To use Keycloak, you need to know your relevant ``realm``. The discovery URL has the form
``https://keycloak.gemeente.nl/auth/realms/${realm}/.well-known/openid-configuration``.
