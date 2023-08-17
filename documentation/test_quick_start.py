from mutwo import music_events
tone = music_events.NoteLike('cs2', 2, 'f')
chord = music_events.NoteLike('c3 e3 g3', 1, 'pp')
rest = music_events.NoteLike([], 1)


from mutwo import core_events
from mutwo import music_events

melody = core_events.SequentialEvent([music_events.NoteLike('c', 1), music_events.NoteLike('d', 0.5), music_events.NoteLike('e', 1)])

reversed_melody = melody.copy()
reversed_melody.reverse()

polyphony = core_events.SimultaneousEvent([melody, reversed_melody])


from mutwo import midi_converters
mc = midi_converters.EventToMidiFile()
mc.convert(polyphony, 'polyphony.mid')


from mutwo import abjad_converters
import abjad
ac = abjad_converters.SequentialEventToAbjadVoice()
s0 = abjad.Staff([ac.convert(polyphony[0])])
s1 = abjad.Staff([ac.convert(polyphony[1])])
score = abjad.Score([s0, s1])
lilypond_file = abjad.LilyPondFile()
lilypond_file.items.append(score)
abjad.persist.as_pdf(lilypond_file, 'polyphony.pdf')
