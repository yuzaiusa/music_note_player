"""
You have managed to play some notes in Exercise 1. Now, let's build on that to play a "sheet music" score.

Our simplied sheet music is a string that contains note names, their lengths, and the tempo. 

The format is as follows:
    <note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>

For example, the first measure of Twinkle Twinkle Little Star in C major can be represented as:
    C4/1.0,C4/1.0,G4/1.0,G4/1.0,A4/1.0,A4/1.0,G4/2.0

Where each note is followed by its length in beats, and the notes are separated by commas.

Your task is to implement a function `play_score` that takes a PyAudio stream, a string representing the score,
and a tempo in beats per minute (BPM). The function should parse the score string (hint: use the split function),
convert it into note-length pairs, and then use the play_note function from exercise1b to play.

Remember to start the audio stream before playing any notes and stop it after you finish playing all the notes.
"""
import pyaudio
from typing import Dict, List, Optional, Union
from helper_functions import start_play, stop_play

def play_score(stream: pyaudio.Stream, score: str, tempo: int):
    """
    Play a score given a set of parameters
    :param stream: PyAudio stream object
    :param score: Score string in the format "<note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>"
    :param tempo: Tempo in beats per minute (BPM) for a quarter note
    :return: None
    """
    pass  # TODO: implement this function

if __name__ == "__main__":
    pass  # TODO: implement here

"""
Tips:
The focus of this exercercise is to practice built-in string operations and function calls. You can find
a comprehensive list of string operations in: https://www.w3schools.com/python/python_ref_string.asp

Useful functions for this exercise is split. For the following exercises, you will also need learn to use
startswith, endswith, strip, join and replace.
"""