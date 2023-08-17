Installation
============

:mod:`mutwo` is written and used in the programming language `Python <https://www.python.org/>`_.
You need to have Python 3.10 or any later version to use *mutwo*.
Perhaps your machine already has Python installed, if not `consult the Python documentation <https://www.python.org/about/gettingstarted/>`_.
To check whether you python version is new enough, simply run:

.. code-block:: sh

    python3 --version

Python dependencies
###################

*Mutwo* packages are available on the `Python package ecosystem pypi <https://pypi.org/>`_ and can be installed via `the package installer pip <https://pip.pypa.io/en/stable/>`_.
*Mutwo* doesn't consist of one single package, but is split into small packages where each of those packages fulfill only one specific purpose.
In this way users only need to install the functionality they need and *mutwo* becomes easily extendable.
All *mutwo* packages depend on the fundamental `mutwo.core <https://pypi.org/project/mutwo.core/>`_ package.

.. code-block:: sh

    pip3 install mutwo.core

In order to use different backends or frontends (midi, abjad, ...) and to have more inner functionality,  *mutwo* needs additional packages.

To represent musical structures in mutwo, you need `mutwo.music <https://pypi.org/project/mutwo.music/>`_:

.. code-block:: sh

    pip3 install mutwo.music

If want to import or export MIDI files, you need to install `mutwo.midi <https://pypi.org/project/mutwo.midi/>`_:

.. code-block:: sh

    pip3 install mutwo.midi

Other dependencies
##################

Some export or import functionalities need additional software that isn't automatically installed when using pip.
You need to manually install this additional software by either using your OS package manager (Linux) or by downloading and installing precompiled binaries (OSX, Windows)

To use the Csound converter, install `Csound <https://csound.com/>`_ first.
To use Lilypond via mutwos abjad converter (`mutwo.abjad <https://pypi.org/project/mutwo.abjad/>`_), install `Lilypond <https://lilypond.org/>`_ first.

Use nix to install python and other dependencies together
#########################################################

Alternatively to pip and your OS package manager, you can use the package manager `Nix <https://nixos.org/>`_ to install all *mutwo* dependencies together.
*Mutwo* has `its own repo <https://github.com/mutwo-org/mutwo-nix>`_ for the packages.

Operating system
################

*mutwo* is tested on Linux, but may equally well work on OSX or Windows.
