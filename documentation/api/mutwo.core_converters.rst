
mutwo.core_converters
=====================

.. contents:: Table of content
   :depth: 3

.. automodule:: mutwo.core_converters
   :members:


.. list-table::
   :width: 95%
   :header-rows: 1

   * - Object
     - Documentation
   * - :class:`mutwo.core_converters.SimpleEventToAttribute`
     - Extract from a simple event an attribute.
   * - :class:`mutwo.core_converters.dict`
     - dict() -> new empty dictionary
   * - :class:`mutwo.core_converters.MutwoParameterDictToKeywordArgument`
     - Extract from a dict of mutwo parameters specific objects.
   * - :class:`mutwo.core_converters.MutwoParameterDictToDuration`
     - Extract from a dict of mutwo parameters the duration.
   * - :class:`mutwo.core_converters.MutwoParameterDictToSimpleEvent`
     - Convert a dict of mutwo parameters to a :class:`mutwo.core_events.SimpleEvent`
   * - :class:`mutwo.core_converters.UnknownObjectToObject`
     - Helper to simplify standardisation of syntactic sugar.
   * - :class:`mutwo.core_converters.TempoPointConverter`
     - Convert a :class:`~mutwo.parameters.tempos.TempoPoint` with BPM to beat-length-in-seconds.
   * - :class:`mutwo.core_converters.TempoConverter`
     - Apply tempo curves on mutwo events
   * - :class:`mutwo.core_converters.EventToMetrizedEvent`
     - Apply tempo envelope of event on itself




.. autoclass:: SimpleEventToAttribute
        .. autoclasstoc::
    

.. autoclass:: dict
        .. autoclasstoc::
    

.. autoclass:: MutwoParameterDictToKeywordArgument
        .. autoclasstoc::
    

.. autoclass:: MutwoParameterDictToDuration
        .. autoclasstoc::
    

.. autoclass:: MutwoParameterDictToSimpleEvent
        .. autoclasstoc::
    

.. autoclass:: UnknownObjectToObject
        .. autoclasstoc::
    

.. autoclass:: TempoPointConverter
        .. autoclasstoc::
    

.. autoclass:: TempoConverter
        .. autoclasstoc::
    

.. autoclass:: EventToMetrizedEvent
        .. autoclasstoc::
    


mutwo.core_converters.abc
-------------------------

.. automodule:: mutwo.core_converters.abc
   :members:


mutwo.core_converters.configurations
------------------------------------

.. automodule:: mutwo.core_converters.configurations
   :members:

