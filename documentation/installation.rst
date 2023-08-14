Installation
============

pypi
####

Mutwo is available on pypi and can be installed via pip.
Because mutwo is split into different packages there are many packages which can be installed depending on the specific use case.
Nevertheless all mutwo packages depend on the basic 'mutwo.core' package.

.. code-block:: sh

    pip3 install mutwo.core

For using different backends or frontends (midi, abjad, ...) mutwo may need additional packages.

.. code-block:: sh

    pip3 install mutwo.midi

Depending on the used converter classes, mutwo may need additional software to work properly.
For using the Csound converter, you should install `Csound https://csound.com/`_ first.
For using Lilypond via mutwos abjad Converter, install `Lilypond https://lilypond.org/`_ first.
For using the ISiS converter, install `ISiS https://isis-documentation.readthedocs.io/en/latest/Intro.html`_ first.


nix
###

Alternatively you can use the package manager `Nix https://nixos.org/`_ to install mutwo.
Mutwo has `its own repo https://github.com/mutwo-org/mutwo-nix`_ for the packages.
