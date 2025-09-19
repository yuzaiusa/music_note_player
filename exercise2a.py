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
