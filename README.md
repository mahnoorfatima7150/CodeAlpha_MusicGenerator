# AI Music Generator

A simple AI-based music generator that creates new melodies from MIDI files using Python and the `music21` library.

---

## Features

* Reads MIDI input file
* Extracts musical notes and chords
* Generates new music patterns
* Saves generated music as a MIDI file
* Includes demo video output

---

## How It Works

* MIDI file (`song.mid`) is parsed using `music21`
* Notes and chords are extracted from the file
* Random note sequences are generated
* A new music stream is created
* Output is saved as `output.mid`

---

## Project Structure

```
.
├── src/
│   └── music_generator.py
├── outputs/
│   ├── music.mp4
│   ├── output.mid
│   ├── song.mid
│   └── yolov8n.pt
├── requirements.txt
└── README.md
```

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python src/music_generator.py
```

---

## 🎥 Demo

Check the demo video:
[Watch Demo](outputs/music.mp4)

---

## Output

Generated music file:
`outputs/output.mid`

---

## Technologies Used

* Python
* music21

---

## Note

Make sure `song.mid` is present inside the `outputs/` folder before running the code.

---

## Author

Mahnoor Fatima
