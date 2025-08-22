"""
You have developed a few useful functions to play notes and scores in previous exercises.

You may have noticed a few inconveniences in the way you have been using these functions:
1. You have to start and stop the audio stream every time you play a note or a score.
2. You have to pass the tempo every time you play a score.
3. You have to finish the score in one go. There is no way to build up a score piece by piece 
and replay later.

It would be nice if you can forget about setting up the audio stream and only set the tempo once.
Also, it would be nice if you can build up your scores by adding pieces to an internal cache or
remove the last added piece if you made a mistake. Finally, it would be nice if you can replay
the whole internal cache of scores at once.

This is where a class can help. Class can encapsulate the data (member variables) and the functions
(member methods) that operate on the data. Class remembers the state of its member variables and member
methods can operate on the member variables without needing to pass them as parameters every time. 
For example, Tempo can be a member variable that be memerized once it is set. The audio stream can be a 
member variable that is set up once when the class instance is created. The internal cache of scores can
be a member variable that is initialized when the class instance is created and be modified by member 
methods to add/remove pieces.

Your task is to implement a class `MusicNotePlayer` that does all the things mentioned above.

In the beginning, you will need to implement the class with the following methods:
- `__init__(self, sample_rate: int = 44100)`: Initialize the player with a sample rate and start the audio stream.
- `set_tempo(self, tempo: int)`: Set the tempo for playback.
- `play_note(self, note: str, length: float)`: Set the tempo for playback.
- `play_score(self, score: str)`: Play a score given as a string.
- `play_score_file(self, filename: str)`: Play a score from a file.

    To properly close the audio stream, some "gargagge collection (GC)" methods need to be implemented.
    This is beyond the scope of this exercise. Please just keep the following methods, don't need to worry
    about the implementation details:
    - `start(self)`: Start the audio stream.
    - `close(self)`: Stop the audio stream.
    - `__exit__(self)`: Ensure the audio stream is properly closed when the instance is gone.

The next step is to allow adding and removing scores. The internal cache will be a list of scores (strings).
The cache should be initialized in __init__ and should be empty at the start. Implement the following methods:
- `add_score(self, score: str)`: Add a score to the internal cache for later playback.
_ `add_score_file(self, filename: str)`: Add a score from a file to the internal cache.
_ `undo_add_score(self)`: Remove the last added score from the internal cache.
- `get_scores(self) -> str`: Get the current internal cache of scores as a string.
- `replay(self)`: Replay the whole internal cache of scores.
- `reset(self)`: Clear the internal cache of scores.
"""

from contextlib import AbstractContextManager
import pyaudio
from time import sleep
from typing import Dict, List, Optional, Union

from helper_functions import start_play, stop_play, play_frequency
from exercise1b import piano_note_frequencies

# Don't need to worry about the class inheritance here
# AbstractContextManager helps provide convenient functions for resource management
class MusicNotePlayer(AbstractContextManager):
    def __init__(self, tempo: int = 60, sample_rate: float = 44100, amplitude: float = 1.0, pause_fraction: float = 0.5, max_pause_duration: float = 0.5):
        # TODO: initialize your internal variables here

        # The rest part of __init__ is for resource managing. Please don't modify
        self._closed = True
        self.start()

    def set_tempo(self, tempo: int):
        pass # TODO: implement

    def play_note(self, note: str, length: float):
        """
        Play a piano note given a set of parameters
        :param note: Note to be played (e.g., 'C4', 'D#5', 'Bb3')
        :param length: Duration of the note in beats (e.g., 1.0 for a quarter note, 0.5 for an eighth note)
        """
        pass # TODO: implement
        
    def play_score(self, score: str):
        pass # TODO: implement

    def play_score_file(self, filename: str, reset_tempo: bool = False):
        pass # TODO: implement
                    
    def add_score(self, score: str):
        pass # TODO: implement
        
    def add_score_file(self, filename: str):
        pass # TODO: implement
        
    def undo_add_score(self):
        pass # TODO: implement
        
    def get_scores(self) -> str:
        pass # TODO: implement
        
    def replay(self):
        pass # TODO: implement
        
    def reset(self):
        pass # TODO: implement
    
    # The rest is for resource managing. Please don't modify
    def start(self):
        # don't start twice
        if self._closed:
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=pyaudio.paFloat32, # Use float32 format for audio data
                                    channels=1,               # Mono audio
                                    rate=self.sample_rate,         # Set up the sample rate
                                    output=True)
            self._closed = False
        
    def close(self):
        # don't close twice
        if self._closed:
            return

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self._closed = True

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False  # don’t suppress exceptions


if __name__ == "__main__":
    """
    Once you have implemented the class, test its functionality one by one. It would be easier if you
    tried it in a jupyter notebook. To use this class in a jupyter notebook, you need to import:
        from exercise3a import MusicNotePlayer

    Eventually, you can play with it in your jupyter notebook or here like this:
        filename = "sample_score.txt"
        with MusicNotePlayer(tempo=60) as p:
            p.play_score_file(filename)

    Or, you can play with adding/removing scores like this:
        with MusicNotePlayer(tempo=60) as p:
            p.add_score("A4/0.25,B4/0.25,C5/0.75,B4/0.25,C5/0.5,E5/0.5,B4/1.5")
            p.replay()
            p.add_score("A4/0.25,B4/0.25,C5/0.75,B4/0.25,C5/0.5,E5/0.5,B4/1.5,E4/0.5,A4/0.75,G4/0.25,A4/0.5,C5/0.5,G4/1.5,E4/0.5,F4/0.5,C5/0.25,B4/0.75,C5/0.5,D5/0.5,E5/0.25,C5/1.25,C5/0.375,B4/0.375,A4/1,B4/1,G#4/1,A4/4")
            p.replay()
            print(p.get_scores())
            p.undo_add_score()
            p.replay()
            p.reset()
            p.replay()
    """
    pass  # TODO: implement here