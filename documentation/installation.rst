Installation
============

Mutwo is available on `pypi <https://pypi.org/project/mutwo/>`_ and can be installed via pip:

.. code-block:: sh

    pip3 install mutwo.ext-core

For using different backends or frontends (midi, abjad, ...) mutwo may need additional extensions.

.. code-block:: sh

    pip3 install mutwo.ext-midi

Depending on the used converter classes, mutwo may need additional software to work properly. For using the Csound converter, you should install Csound first. For using Lilypond via mutwos abjad Converter, install Lilypond first. For using the ISiS converter, install ISiS first.
