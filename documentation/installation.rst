Installation
============

Mutwo is available on pypi and can be installed via pip.
Because mutwo is split into different packages there are many packages which can be installed depending on the specific use case.
Nevertheless all mutwo packages depend on the basic 'mutwo.core' package.

.. code-block:: sh

    pip3 install mutwo.core

For using different backends or frontends (midi, abjad, ...) mutwo may need additional packages.

.. code-block:: sh

    pip3 install mutwo.midi

Depending on the used converter classes, mutwo may need additional software to work properly. For using the Csound converter, you should install Csound first. For using Lilypond via mutwos abjad Converter, install Lilypond first. For using the ISiS converter, install ISiS first.
