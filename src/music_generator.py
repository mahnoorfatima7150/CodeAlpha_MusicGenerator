import music21
import random
print(" Music Generator Started")
file = "song.mid"
try:
    midi = music21.converter.parse(file)
except:
    print(" Error: MIDI file not found. Make sure 'song.mid' is in the folder.")
    exit()
notes = []
for element in midi.flat.notes:
    if isinstance(element, music21.note.Note):
        notes.append(str(element.pitch))
    elif isinstance(element, music21.chord.Chord):
        notes.append('.'.join(str(n) for n in element.normalOrder))
print(f" Extracted {len(notes)} notes")
generated = []
for i in range(50):
    generated.append(random.choice(notes))
output_notes = []
for pattern in generated:
    if '.' in pattern:
        notes_in_chord = pattern.split('.')
        chord_notes = []
        for n in notes_in_chord:
            try:
                new_note = music21.note.Note(int(n))
                chord_notes.append(new_note)
            except:
                continue
        if chord_notes:
            new_chord = music21.chord.Chord(chord_notes)
            output_notes.append(new_chord)
    else:
        try:
            new_note = music21.note.Note(pattern)
            output_notes.append(new_note)
        except:
            continue
stream = music21.stream.Stream(output_notes)
stream.write('midi', fp='output.mid')
print("Music generated successfully!")
print("File saved as: output.mid")
