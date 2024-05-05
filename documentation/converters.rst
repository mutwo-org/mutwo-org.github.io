.. _converters:

Understanding converters
========================

With :ref:`parameters` we are now able to actually describe some meaningful musical content in *mutwo*.
But what's the purpose to describe this musical content if it only resides in our text file or python interpreter?

This is where **converters** are needed:
by using converters :mod:`mutwo` communicates with the outer world.
Some converters import data into :mod:`mutwo` and some converters export data from :mod:`mutwo` into another format.

Finally there are converters that translate between two different data types within *mutwo*.
For instance, if we want to write a transposed score for a `transposing instrument <https://en.wikipedia.org/wiki/Transposing_instrument>`_, we may want to use a converter which translates from the sounding music to the written music.

Using the MIDI converter
########################

In order to illustrate converters, let's export our musical content to a `Standard MIDI file <https://www.midi.org/specifications-old/item/standard-midi-files-smf>`_.
For this example, you need to install the `mutwo.midi <https://pypi.org/project/mutwo.midi/>`_ package.

Let's first define a small melody that we export to the MIDI file:

.. code-block:: python

   from mutwo import core_events
   from mutwo import music_events

   melody = core_events.Consecution(
       [
           music_events.NoteLike('c', 0.25),
           music_events.NoteLike('e', 0.5),
           music_events.NoteLike('d', 0.25),
           music_events.NoteLike('c', 1),
       ]
   )


Now let's convert this melody to MIDI:

.. code-block:: python

   from mutwo import midi_converters

   e2m = midi_converters.EventToMidiFile()
   e2m.convert(melody, 'melody.mid')


By using a MIDI player (for instance `TiMidity++ <https://timidity.sourceforge.net/>`_) we can listen to this melody now:

.. raw:: html

    <audio controls="controls">
      <source src="melody.ogg" type="audio/ogg">
      Your browser does not support the <code>audio</code> element. 
    </audio>




