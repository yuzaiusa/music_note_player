"""
You have developed a few useful functions to play notes and scores in previous exercises.

It would be nice if you can package these functions into a class so that you can easily add
scores piece by piece and replay them later.

Also, you used to start and stop the audio stream every time you play a note or a score.
Now, you can start the audio stream once when you create an instance of the class and stop it
when you are done with all the playing.

Your task is to implement a class `MusicNotePlayer` that has the following methods:
- `__init__(self, sample_rate: int = 44100)`: Initialize the player with a sample rate and start the audio stream.
- `play_score(self, score: str, tempo: int)`: Play a score given as a string.
- `play_score_file(self, filename: str)`: Play a score from a file.
- `add_score(self, score: str)`: Add a score to the internal cache for later playback.
_ `add_score_file(self, filename: str)`: Add a score from a file to the internal cache.
- `set_tempo(self, tempo: int)`: Set the tempo for playback.
- `replay(self)`: Replay the whole internal cache of scores.
- `reset(self)`: Clear the internal cache of scores.
- `stop(self)`: Stop the audio stream.
- `__del__(self)`: Ensure the audio stream is properly closed when the instance is deleted.

Remember to handle __del__ to  ensure that the audio stream is properly closed when deleted.

You can use the functions from previous exercises as methods in this class.
"""
import pyaudio
from typing import Dict
from helper_functions import play_frequency, start_play, stop_play

class MusicNotePlayer:
    pass  # TODO: implement this class

if __name__ == "__main__":
    pass  # TODO: implement here