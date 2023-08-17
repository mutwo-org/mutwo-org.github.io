from mutwo import core_events
from mutwo import music_events

melody = core_events.SequentialEvent(
    [
        music_events.NoteLike('c', 0.25),
        music_events.NoteLike('e', 0.5),
        music_events.NoteLike('d', 0.25),
        music_events.NoteLike('c', 1),
    ]
)

from mutwo import midi_converters

e2m = midi_converters.EventToMidiFile()
e2m.convert(melody, 'melody.mid')

