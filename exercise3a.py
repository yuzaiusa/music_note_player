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
    pass  # TODO: implement here
