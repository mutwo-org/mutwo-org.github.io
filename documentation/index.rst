.. mutwo documentation master file, created by
   sphinx-quickstart on Wed Feb  3 23:07:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mutwo's documentation!
=================================

**Mutwo** is a flexible, event based framework for composing music or other time-based arts in Python. It aims to help composers to build musical structures in a meaningful way and translate those structures to different third party objects (e.g. midi files, `csound <http://www.csounds.com/>`_ scores, musical notation with `Lilypond <https://lilypond.org/>`_ via `Abjad <https://github.com/Abjad/abjad>`_). The general design philosophy stresses out the independence and freedom of the user with the help of generic data structures and an easily extensible and tweakable software design.

The following example generates a short midi file:

.. code-block:: python

    from mutwo import core_events
    from mutwo import music_events
    from mutwo import midi_converters
    simple_melody = core_events.SequentialEvent(
        [
            music_events.NoteLike(pitch_name, duration=duration, volume="mf")
            for pitch_name, duration in (
                ("c", 0.75),
                ("a", 0.25),
                ("g", 1 / 6),
                ("es", 1 / 12),
            )
        ]
    )
    event_to_midi_file = midi_converters.EventToMidiFile()
    event_to_midi_file.convert(simple_melody, "my_simple_melody.mid")


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   introduction
   api/api_documentation
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
