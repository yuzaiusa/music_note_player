"""
In excercise 2a, you implemented a function to play a line of sheet music given as a string.
Now, let's build on that to play the whole song by taking the score from a text file.

Your task is to implement a function `play_score_file` that takes a PyAudio stream and a filename.
The function should read the score from the file, parse it into a string that can be passed to the 
`play_score` function from exercise2a.

The format of the score file is as follows:
    title: <tile of the song>
    tempo: <tempo in beats per minute (BPM)>
    score: <score string in the format "<note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>">

For example, a score file for the first measure of Twinkle Twinkle Little Star in C major might look like this:
    title: Twinkle Twinkle Little Star
    tempo: 120
    score: C4/1.0,C4/1.0,G4/1.0,G4/1.0,A4/1.0,A4/1.0,G4/2.0

You can find the score file `sample_score.txt` in the same directory as this exercise file.

Remember to open the file within a with statement to ensure it is properly closed after reading.

Remember to start the audio stream before playing any notes and stop it after you finish playing all the notes.
"""
import pyaudio
from typing import Dict, List, Optional, Union
from helper_functions import start_play, stop_play

def play_score_file(stream: pyaudio.Stream, filename: str, tempo: int):
    """
    Play a score from a file given a set of parameters
    :param stream: PyAudio stream object
    :param filename: Name of the file containing the score string in the format "<note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>"
    :param tempo: Tempo in beats per minute (BPM) for a quarter note
    :return: None
    """
    pass  # TODO: implement this function

if __name__ == "__main__":
    pass  # TODO: implement here
