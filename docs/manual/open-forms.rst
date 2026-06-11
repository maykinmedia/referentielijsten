


Integratie met Open-formulieren
===============================
`Open Formulieren documentatie <https://open-forms.readthedocs.io/en/stable/manual/forms/form_fields.html#id3>`_
Referentielijsten kunnen in Open Formulieren worden gebruikt om de velden ``keuzelijst``, ``selectievakjes`` & ``radio`` te vullen.

Voorbeeld
~~~~~~~~~

    #. Voeg de referentielijst als een service toe aan open-formulieren

        .. image:: assets/service.png
            :width: 100%
            :alt: Service


    #. Voeg een radio component toe aan een formulier
    #. selecteer bij ``Keuzeopties`` ``Reference lists API``

        .. image:: assets/radio.png
            :width: 100%
            :alt: Radio

    #. selecteer de service referentielijst service in ``Service``
    #. selecteer de code van de tabel die het component moet gebruiken in ``Tabelcode``

        .. image:: assets/tabelcode.png
            :width: 100%
            :alt: Tabelcode

    #. sla het component op.
    #. In het formulier worden de items uit de tabel in de radio component geladen.

        .. image:: assets/form.png
            :width: 100%
            :alt: Form





