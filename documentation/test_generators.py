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

from mutwo import midi_converters

midi_converters.EventToMidiFile(available_midi_channel_tuple=tuple(range(5))).convert(
    event, "generated.mid"
)
