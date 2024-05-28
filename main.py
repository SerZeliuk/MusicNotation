import sys
from antlr4 import *
from MusicNotationLexer import MusicNotationLexer
from MusicNotationParser import MusicNotationParser
from music21 import stream, note, chord, duration, tempo, key, environment, instrument
import tkinter as tk
from tkinter import scrolledtext

class MusicNotationListener(ParseTreeListener):
    def __init__(self):
        self.stream = stream.Score()
        self.current_part = stream.Part()
        self.current_part.append(instrument.fromString(' '))
        self.stream.append(self.current_part)

    def enterKey(self, ctx: MusicNotationParser.KeyContext):
        key_signature = ctx.getText().split('=')[1]
        self.current_part.append(key.Key(key_signature))

    def enterTempo(self, ctx: MusicNotationParser.TempoContext):
        bpm = int(ctx.getText().replace('bpm', ''))
        self.current_part.append(tempo.MetronomeMark(number=bpm))

    def enterMeasure(self, ctx: MusicNotationParser.MeasureContext):
        if self.current_part.notes:
            self.current_part.append(stream.Measure())

    def enterNote_or_chord(self, ctx: MusicNotationParser.Note_or_chordContext):
        notes = []
        children = list(ctx.getChildren())
        for i in range(0, len(children), 4):
            note_text = ''.join([children[j].getText() for j in range(i, i+4) if j < len(children)])
            print("rere:" + note_text)
            if len(note_text) >= 3:
                pitch = note_text[0].upper() + note_text[1]  # note and octave
                dur = note_text[2]  # duration
                duration_type = self.convert_duration(dur)
                n = note.Note(pitch)
                n.duration.type = duration_type
                notes.append(n)
                
        if len(notes) > 1:
            self.current_part.append(chord.Chord(notes))
        elif notes:
            self.current_part.append(notes[0])

    def enterRest(self, ctx: MusicNotationParser.RestContext):
        dur = ctx.getChild(1).getText()  # duration
        duration_type = self.convert_duration(dur)
        r = note.Rest(type=duration_type)
        self.current_part.append(r)

    def convert_duration(self, dur):
        duration_map = {
            'w': 'whole',
            'h': 'half',
            'q': 'quarter',
            'e': 'eighth',
            's': '16th',
            't': '32nd'
        }
        return duration_map.get(dur, 'quarter')

def parse_and_show(input_text):
    input_stream = InputStream(input_text)
    lexer = MusicNotationLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MusicNotationParser(token_stream)
    tree = parser.music()

    listener = MusicNotationListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    listener.stream.show('midi')
    # listener.stream.show('musicxml')

def on_parse_button_click():
    input_text = text_area.get("1.0", tk.END)
    print(input_text)
    parse_and_show(input_text)

# Setting up the GUI

env = environment.Environment()
env['musicxmlPath'] = 'C:\\Program Files\\MuseScore 4\\bin\\MuseScore4.exe'  # Adjust the path as necessary

root = tk.Tk()
root.title("Music Notation Parser")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter Music Notation:")
label.pack(anchor="w")

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10)
text_area.pack(padx=10, pady=10)

parse_button = tk.Button(frame, text="Parse and Show", command=on_parse_button_click)
parse_button.pack(pady=10)

root.mainloop()
