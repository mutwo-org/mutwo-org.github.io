Cookbook
========

This is a collection of small How-Tos in the *mutwo* framework.

Define your events by name
##########################

You can use :class:`~mutwo.core_events.TaggedSequentialEvent` or :class:`~mutwo.core_events.TaggedSimultaneousEvent`:

.. code-block:: python

   from mutwo import core_events

   e = core_events.SimultaneousEvent(
       [core_events.TaggedSequentialEvent([], tag="a", core_events.TaggedSimultaneousEvent([], tag="b"]
   )

   # We can access events by tags
   e['a'] == e[0]

Set concert pitch
#################

You can set the concert pitch locally:

.. code-block:: python

   from mutwo import music_parameters

   music_parameters.WesternPitch('c', 4, concert_pitch=443)

But you can also set it globally:

.. code-block:: python

   from mutwo import music_parameters

   music_parameters.configurations.DEFAULT_CONCERT_PITCH = 443

Make a glissando
################

All pitches have a pitch envelope.
This pitch envelope defines a glissando:
you can specify how much the pitch should derive in cents from the original frequency.

.. code-block:: python

   from mutwo import music_parameters

   pitch_with_gliss = music_parameters.DirectPitch(300, envelope=[[0, 0], [1, -100], [2, 100], [3, 0]])


Set and apply tempo of your event
#################################

All events have a :attr:`~mutwo.core_events.abc.Event.tempo_envelope` attribute, which can be set in order to change the tempo of your event:

.. code-block:: python

   from mutwo import core_events

   e = core_events.SimpleEvent(duration=1, tempo_envelope=[[0, 60], [1, 30]])

   # Apply tempo envelope on event:
   e.metrize()

Write polytempic music
######################

Because each :class:`~mutwo.core_events.abc.Event` has its own :class:`~mutwo.core_events.TempoEnvelope`, it's very easy to describe polytempic music:

.. code-block:: python

   from mutwo import core_events

   e = core_events.SimultaneousEvent(
       [
           core_events.SequentialEvent([], tempo_envelope=[[0, 60], [1, 30]]),
           core_events.SequentialEvent([], tempo_envelope=[[0, 40], [1, 90]]),
       ]
   )


Change all pitches / volumes / ... of a :class:`~mutwo.core_events.SequentialEvent` or :class:`~mutwo.core_events.SimultaneousEvent`
####################################################################################################################################

You can use :meth:`~mutwo.core_events.abc.Event.set_parameter` or :meth:`~mutwo.core_events.abc.Event.mutate_parameter` to change a parameter of an event and its children:

.. code-block:: python

   from mutwo import core_events
   from mutwo import music_events
   from mutwo import music_parameters

   e = core_events.SimultaneousEvent(
       [
           core_events.SequentialEvent([music_events.NoteLike('c', 2)]),
           music_events.NoteLike('d', 2),
       ]
   )

   # Set the volume of all 'NoteLike' to 'fff':
   e.set_parameter('volume', music_parameters.WesternVolume('fff'))

   # 'set_parameter' also allows to parse a function
   # which gets the previous value of the parameter.
   #
   # Let's rise all pitches by an octave:
   e.set_parameter(
       'pitch_list',
       lambda pitch_list: pitch_list[0].add(music_parameters.DirectPitchInterval(1200))
   )

