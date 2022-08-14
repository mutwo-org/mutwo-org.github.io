
mutwo.abjad_converters
======================

.. contents:: Table of content
   :depth: 3

.. automodule:: mutwo.abjad_converters
   :members:


.. list-table::
   :width: 95%
   :header-rows: 1

   * - Object
     - Documentation
   * - :class:`mutwo.abjad_converters.SequentialEventToQuantizedAbjadContainer`
     - Quantize :class:`~mutwo.core_events.SequentialEvent` objects.
   * - :class:`mutwo.abjad_converters.NauertSequentialEventToQuantizedAbjadContainer`
     - Quantize :class:`~mutwo.core_events.SequentialEvent` objects via :mod:`abjadext.nauert`.
   * - :class:`mutwo.abjad_converters.NauertSequentialEventToDurationLineBasedQuantizedAbjadContainer`
     - Quantize :class:`~mutwo.core_events.SequentialEvent` objects via :mod:`abjadext.nauert`.
   * - :class:`mutwo.abjad_converters.LeafMakerSequentialEventToQuantizedAbjadContainer`
     - Quantize :class:`~mutwo.core_events.SequentialEvent` object via :mod:`abjad.LeafMaker`.
   * - :class:`mutwo.abjad_converters.LeafMakerSequentialEventToDurationLineBasedQuantizedAbjadContainer`
     - Quantize :class:`~mutwo.core_events.SequentialEvent` object via :mod:`abjad.LeafMaker`.
   * - :class:`mutwo.abjad_converters.ComplexEventToAbjadContainer`
     - 
   * - :class:`mutwo.abjad_converters.SequentialEventToAbjadVoice`
     - Convert :class:`~mutwo.core_events.SequentialEvent` to :class:`abjad.Voice`.
   * - :class:`mutwo.abjad_converters.NestedComplexEventToAbjadContainer`
     - 
   * - :class:`mutwo.abjad_converters.NestedComplexEventToComplexEventToAbjadContainers`
     - 
   * - :class:`mutwo.abjad_converters.CycleBasedNestedComplexEventToComplexEventToAbjadContainers`
     - 
   * - :class:`mutwo.abjad_converters.TagBasedNestedComplexEventToComplexEventToAbjadContainers`
     - 
   * - :class:`mutwo.abjad_converters.MutwoLyricToAbjadString`
     - 
   * - :class:`mutwo.abjad_converters.MutwoPitchToAbjadPitch`
     - Convert Mutwo Pitch objects to Abjad Pitch objects.
   * - :class:`mutwo.abjad_converters.TempoEnvelopeToAbjadAttachmentTempo`
     - Convert tempo envelope to :class:`~mutwo.converters.frontends.abjad_parameters.Tempo`.
   * - :class:`mutwo.abjad_converters.ComplexTempoEnvelopeToAbjadAttachmentTempo`
     - Convert tempo envelope to :class:`~mutwo.converters.frontends.abjad_parameters.Tempo`.
   * - :class:`mutwo.abjad_converters.MutwoVolumeToAbjadAttachmentDynamic`
     - Convert Mutwo Volume objects to :class:`~mutwo.converters.frontends.abjad_parameters.Dynamic`.
   * - :class:`mutwo.abjad_converters.MutwoPitchToHEJIAbjadPitch`
     - Convert Mutwo :obj:`~mutwo.ext.parameters.pitches.JustIntonationPitch` objects to Abjad Pitch objects.
   * - :class:`mutwo.abjad_converters.ProcessAbjadContainerRoutine`
     - 
   * - :class:`mutwo.abjad_converters.AddDurationLineEngraver`
     - 
   * - :class:`mutwo.abjad_converters.PrepareForDurationLineBasedNotation`
     - 
   * - :class:`mutwo.abjad_converters.AddInstrumentName`
     - 
   * - :class:`mutwo.abjad_converters.AddAccidentalStyle`
     - 
   * - :class:`mutwo.abjad_converters.SetStaffSize`
     - 




.. autoclass:: mutwo.abjad_converters.SequentialEventToQuantizedAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.NauertSequentialEventToQuantizedAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.NauertSequentialEventToDurationLineBasedQuantizedAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.LeafMakerSequentialEventToQuantizedAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.LeafMakerSequentialEventToDurationLineBasedQuantizedAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.ComplexEventToAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.SequentialEventToAbjadVoice
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.NestedComplexEventToAbjadContainer
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.NestedComplexEventToComplexEventToAbjadContainers
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.CycleBasedNestedComplexEventToComplexEventToAbjadContainers
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.TagBasedNestedComplexEventToComplexEventToAbjadContainers
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.MutwoLyricToAbjadString
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.MutwoPitchToAbjadPitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.TempoEnvelopeToAbjadAttachmentTempo
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.ComplexTempoEnvelopeToAbjadAttachmentTempo
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.MutwoVolumeToAbjadAttachmentDynamic
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.MutwoPitchToHEJIAbjadPitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.ProcessAbjadContainerRoutine
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.AddDurationLineEngraver
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.PrepareForDurationLineBasedNotation
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.AddInstrumentName
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.AddAccidentalStyle
        .. autoclasstoc::
    

.. autoclass:: mutwo.abjad_converters.SetStaffSize
        .. autoclasstoc::
    


mutwo.abjad_converters.configurations
-------------------------------------

.. automodule:: mutwo.abjad_converters.configurations
   :members:

