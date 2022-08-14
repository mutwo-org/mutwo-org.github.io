
mutwo.core_events
=================

.. contents:: Table of content
   :depth: 3

.. automodule:: mutwo.core_events
   :members:


.. list-table::
   :width: 95%
   :header-rows: 1

   * - Object
     - Documentation
   * - :class:`mutwo.core_events.SimpleEvent`
     - Event-Object which doesn't contain other Event-Objects (the node or leaf).
   * - :class:`mutwo.core_events.SequentialEvent`
     - Event-Object which contains other Events which happen in a linear order.
   * - :class:`mutwo.core_events.SimultaneousEvent`
     - Event-Object which contains other Event-Objects which happen at the same time.
   * - :class:`mutwo.core_events.TaggedSimpleEvent`
     - :class:`SimpleEvent` with tag.
   * - :class:`mutwo.core_events.TaggedSequentialEvent`
     - :class:`SequentialEvent` with tag.
   * - :class:`mutwo.core_events.TaggedSimultaneousEvent`
     - :class:`SimultaneousEvent` with tag.
   * - :class:`mutwo.core_events.Envelope`
     - Model continuous changing values (e.g. glissandi, crescendo).
   * - :class:`mutwo.core_events.RelativeEnvelope`
     - Envelope with relative durations and values / parameters.
   * - :class:`mutwo.core_events.TempoEnvelope`
     - 




.. autoclass:: mutwo.core_events.SimpleEvent
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.SequentialEvent
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.SimultaneousEvent
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.TaggedSimpleEvent
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.TaggedSequentialEvent
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.TaggedSimultaneousEvent
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.Envelope
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.RelativeEnvelope
        .. autoclasstoc::
    

.. autoclass:: mutwo.core_events.TempoEnvelope
        .. autoclasstoc::
    


mutwo.core_events.abc
---------------------

.. automodule:: mutwo.core_events.abc
   :members:


mutwo.core_events.configurations
--------------------------------

.. automodule:: mutwo.core_events.configurations
   :members:

