Understanding generators
========================

In :ref:`converters` we could export our musical content and listen to it.
The musical content itself was very short and plain.
Now we could of course simply write a very long text file in which we manually and imperatively define our more comprehensive event.
But since we are using a programming language, `generative approaches <https://en.wikipedia.org/wiki/Generative_art>`_ and more concretely `algorithmic approaches <https://en.wikipedia.org/wiki/Algorithmic_art>`_ are easy to apply.
One possibility to apply such an approach is managed by functionalities that are named **generators** in *mutwo*.
Generators are simply small procedures that generate some data which can be interpreted as musical content by the composer.

The package `mutwo.common <https://pypi.org/project/mutwo.common/>`_ hosts some historically defined algorithms.
We could for instance use :class:`~mutwo.common_generators.ActivityLevel` and :meth:`~mutwo.common_generators.euclidean` to write a small composition.

.. code-block:: python

    from mutwo import common_generators
    from mutwo import core_events
    from mutwo import music_events
    from mutwo import music_parameters

    beat_count = (3, 5, 4, 5, 6, 2)
    activity_level = common_generators.ActivityLevel()

    event = core_events.Concurrence([])

    for pitch_list, bc in (
        (
            [
                music_parameters.JustIntonationPitch("1/2"),
                music_parameters.JustIntonationPitch("7/16"),
            ],
            beat_count,
        ),
        (
            [
                music_parameters.JustIntonationPitch("7/6"),
                music_parameters.JustIntonationPitch("4/3"),
            ],
            reversed(beat_count),
        ),
    ):
        s = core_events.Consecution([])
        for b in bc:
            rhythm = common_generators.euclidean(7, b)
            for duration in rhythm:
                if activity_level(6):
                    pitch = pitch_list[activity_level(5)]
                else:
                    pitch = []
                n = music_events.NoteLike(pitch, duration, "pp")
                s.append(n)
        event.append(s)

    event.duration *= 1.5

Then let's also export this event to a MIDI file:

.. code-block:: python

    from mutwo import midi_converters

    midi_converters.EventToMidiFile(available_midi_channel_tuple=tuple(range(5))).convert(
        event, "generated.mid"
    )

.. raw:: html

    <audio controls="controls">
      <source src="generated.ogg" type="audio/ogg">
      Your browser does not support the <code>audio</code> element. 
    </audio>

(rendered with `TiMidity++ <https://timidity.sourceforge.net/>`_)

