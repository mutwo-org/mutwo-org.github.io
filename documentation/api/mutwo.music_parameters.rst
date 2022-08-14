
mutwo.music_parameters
======================

.. contents:: Table of content
   :depth: 3

.. automodule:: mutwo.music_parameters
   :members:


.. list-table::
   :width: 95%
   :header-rows: 1

   * - Object
     - Documentation
   * - :class:`mutwo.music_parameters.OctaveAmbitus`
     - 
   * - :class:`mutwo.music_parameters.Comma`
     - A `tuning comma <https://en.wikipedia.org/wiki/Comma_(music)>`_.
   * - :class:`mutwo.music_parameters.CommaCompound`
     - Collection of tuning commas.
   * - :class:`mutwo.music_parameters.DirectLyric`
     - Lyric which is directly initialised by its phonetic representation
   * - :class:`mutwo.music_parameters.LanguageBasedLyric`
     - Lyric based on a natural language.
   * - :class:`mutwo.music_parameters.LanguageBasedSyllable`
     - Syllable based on a natural language.
   * - :class:`mutwo.music_parameters.DirectPitchInterval`
     - Simple interval class which gets directly assigned by its cents value
   * - :class:`mutwo.music_parameters.WesternPitchInterval`
     - Model intervals by using European music theory based representations
   * - :class:`mutwo.music_parameters.DirectPitch`
     - A simple pitch class that gets directly initialised by its frequency.
   * - :class:`mutwo.music_parameters.JustIntonationPitch`
     - Pitch that is defined by a frequency ratio and a reference pitch.
   * - :class:`mutwo.music_parameters.Partial`
     - Abstract representation of a harmonic spectrum partial.
   * - :class:`mutwo.music_parameters.EqualDividedOctavePitch`
     - Pitch that is tuned to an Equal divided octave tuning system.
   * - :class:`mutwo.music_parameters.WesternPitch`
     - Pitch with a traditional Western nomenclature.
   * - :class:`mutwo.music_parameters.MidiPitch`
     - Pitch that is defined by its midi pitch number.
   * - :class:`mutwo.music_parameters.CommonHarmonic`
     - :class:`JustIntonationPitch` which is the common harmonic between two or more other pitches.
   * - :class:`mutwo.music_parameters.DirectVolume`
     - A simple volume class that gets directly initialised by its amplitude.
   * - :class:`mutwo.music_parameters.DecibelVolume`
     - A simple volume class that gets directly initialised by decibel.
   * - :class:`mutwo.music_parameters.WesternVolume`
     - Volume with a traditional Western nomenclature.
   * - :class:`mutwo.music_parameters.BarLine`
     - BarLine(abbreviation: Optional[str] = None)
   * - :class:`mutwo.music_parameters.Clef`
     - Clef(name: Optional[str] = None)
   * - :class:`mutwo.music_parameters.Ottava`
     - Ottava(n_octaves: Optional[int] = 0)
   * - :class:`mutwo.music_parameters.MarginMarkup`
     - MarginMarkup(content: Optional[str] = None, context: Optional[str] = 'Staff')
   * - :class:`mutwo.music_parameters.Markup`
     - Markup(content: Optional[str] = None, direction: Optional[str] = None)
   * - :class:`mutwo.music_parameters.RehearsalMark`
     - RehearsalMark(markup: Optional[str] = None)
   * - :class:`mutwo.music_parameters.NotationIndicatorCollection`
     - NotationIndicatorCollection(bar_line: mutwo.music_parameters.notation_indicators.BarLine = <factory>, clef: mutwo.music_parameters.notation_indicators.Clef = <factory>, ottava: mutwo.music_parameters.notation_indicators.Ottava = <factory>, margin_markup: mutwo.music_parameters.notation_indicators.MarginMarkup = <factory>, markup: mutwo.music_parameters.notation_indicators.Markup = <factory>, rehearsal_mark: mutwo.music_parameters.notation_indicators.RehearsalMark = <factory>)
   * - :class:`mutwo.music_parameters.Tremolo`
     - Tremolo(n_flags: Optional[int] = None)
   * - :class:`mutwo.music_parameters.Articulation`
     - Articulation(name: Optional[Literal['accent', 'marcato', 'staccatissimo', 'espressivo', 'staccato', 'tenuto', 'portato', 'upbow', 'downbow', 'flageolet', 'thumb', 'lheel', 'rheel', 'ltoe', 'rtoe', 'open', 'halfopen', 'snappizzicato', 'stopped', 'turn', 'reverseturn', 'trill', 'prall', 'mordent', 'prallprall', 'prallmordent', 'upprall', 'downprall', 'upmordent', 'downmordent', 'pralldown', 'prallup', 'lineprall', 'signumcongruentiae', 'shortfermata', 'fermata', 'longfermata', 'verylongfermata', 'segno', 'coda', 'varcoda', '^', '+', '-', '|', '>', '.', '_']] = None)
   * - :class:`mutwo.music_parameters.Arpeggio`
     - Arpeggio(direction: Optional[Literal['up', 'down']] = None)
   * - :class:`mutwo.music_parameters.Pedal`
     - Pedal(pedal_type: Optional[Literal['sustain', 'sostenuto', 'corda']] = None, pedal_activity: Optional[bool] = True)
   * - :class:`mutwo.music_parameters.StringContactPoint`
     - StringContactPoint(contact_point: Optional[Literal['dietro ponticello', 'molto sul ponticello', 'molto sul tasto', 'ordinario', 'pizzicato', 'ponticello', 'sul ponticello', 'sul tasto', 'col legno tratto', 'd.p.', 'm.s.p', 'm.s.t.', 'ord.', 'pizz.', 'p.', 's.p.', 's.t.', 'c.l.t.']] = None)
   * - :class:`mutwo.music_parameters.Ornamentation`
     - Ornamentation(direction: Optional[Literal['up', 'down']] = None, n_times: int = 1)
   * - :class:`mutwo.music_parameters.BendAfter`
     - BendAfter(bend_amount: Optional[float] = None, minimum_length: Optional[float] = 3, thickness: Optional[float] = 3)
   * - :class:`mutwo.music_parameters.ArtificalHarmonic`
     - ArtificalHarmonic(n_semitones: Optional[int] = None)
   * - :class:`mutwo.music_parameters.PreciseNaturalHarmonic`
     - PreciseNaturalHarmonic(string_pitch: Optional[mutwo.music_parameters.pitches.WesternPitch.WesternPitch] = None, played_pitch: Optional[mutwo.music_parameters.pitches.WesternPitch.WesternPitch] = None, harmonic_note_head_style: bool = True, parenthesize_lower_note_head: bool = False)
   * - :class:`mutwo.music_parameters.Fermata`
     - Fermata(fermata_type: Optional[Literal['shortfermata', 'fermata', 'longfermata', 'verylongfermata']] = None)
   * - :class:`mutwo.music_parameters.Hairpin`
     - Hairpin(symbol: Optional[Literal['<', '>', '<>', '!']] = None, niente: bool = False)
   * - :class:`mutwo.music_parameters.Trill`
     - Trill(pitch: Optional[mutwo.music_parameters.abc.Pitch] = None)
   * - :class:`mutwo.music_parameters.WoodwindFingering`
     - WoodwindFingering(cc: Optional[Tuple[str, ...]] = None, left_hand: Optional[Tuple[str, ...]] = None, right_hand: Optional[Tuple[str, ...]] = None, instrument: str = 'clarinet')
   * - :class:`mutwo.music_parameters.Cue`
     - Cue for electronics etc.
   * - :class:`mutwo.music_parameters.PlayingIndicatorCollection`
     - PlayingIndicatorCollection(articulation: mutwo.music_parameters.playing_indicators.Articulation = <factory>, artifical_harmonic: mutwo.music_parameters.playing_indicators.ArtificalHarmonic = <factory>, arpeggio: mutwo.music_parameters.playing_indicators.Arpeggio = <factory>, bartok_pizzicato: mutwo.music_parameters.abc.PlayingIndicator = <factory>, bend_after: mutwo.music_parameters.playing_indicators.BendAfter = <factory>, breath_mark: mutwo.music_parameters.abc.PlayingIndicator = <factory>, cue: mutwo.music_parameters.playing_indicators.Cue = <factory>, duration_line_dashed: mutwo.music_parameters.abc.PlayingIndicator = <factory>, duration_line_triller: mutwo.music_parameters.abc.PlayingIndicator = <factory>, fermata: mutwo.music_parameters.playing_indicators.Fermata = <factory>, glissando: mutwo.music_parameters.abc.PlayingIndicator = <factory>, hairpin: mutwo.music_parameters.playing_indicators.Hairpin = <factory>, natural_harmonic: mutwo.music_parameters.abc.PlayingIndicator = <factory>, laissez_vibrer: mutwo.music_parameters.abc.PlayingIndicator = <factory>, ornamentation: mutwo.music_parameters.playing_indicators.Ornamentation = <factory>, pedal: mutwo.music_parameters.playing_indicators.Pedal = <factory>, prall: mutwo.music_parameters.abc.PlayingIndicator = <factory>, precise_natural_harmonic: mutwo.music_parameters.playing_indicators.PreciseNaturalHarmonic = <factory>, string_contact_point: mutwo.music_parameters.playing_indicators.StringContactPoint = <factory>, tie: mutwo.music_parameters.abc.PlayingIndicator = <factory>, tremolo: mutwo.music_parameters.playing_indicators.Tremolo = <factory>, trill: mutwo.music_parameters.playing_indicators.Trill = <factory>, woodwind_fingering: mutwo.music_parameters.playing_indicators.WoodwindFingering = <factory>)




.. autoclass:: mutwo.music_parameters.OctaveAmbitus
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Comma
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.CommaCompound
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.DirectLyric
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.LanguageBasedLyric
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.LanguageBasedSyllable
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.DirectPitchInterval
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.WesternPitchInterval
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.DirectPitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.JustIntonationPitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Partial
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.EqualDividedOctavePitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.WesternPitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.MidiPitch
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.CommonHarmonic
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.DirectVolume
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.DecibelVolume
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.WesternVolume
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.BarLine
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Clef
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Ottava
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.MarginMarkup
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Markup
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.RehearsalMark
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.NotationIndicatorCollection
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Tremolo
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Articulation
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Arpeggio
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Pedal
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.StringContactPoint
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Ornamentation
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.BendAfter
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.ArtificalHarmonic
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.PreciseNaturalHarmonic
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Fermata
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Hairpin
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Trill
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.WoodwindFingering
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.Cue
        .. autoclasstoc::
    

.. autoclass:: mutwo.music_parameters.PlayingIndicatorCollection
        .. autoclasstoc::
    


mutwo.music_parameters.abc
--------------------------

.. automodule:: mutwo.music_parameters.abc
   :members:


mutwo.music_parameters.configurations
-------------------------------------

.. automodule:: mutwo.music_parameters.configurations
   :members:


mutwo.music_parameters.constants
--------------------------------

.. automodule:: mutwo.music_parameters.constants
   :members:

