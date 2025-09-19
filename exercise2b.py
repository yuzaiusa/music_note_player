import pyaudio
from typing import Dict, List, Optional, Union
from helper_functions import start_play, stop_play

def play_score_file(stream: pyaudio.Stream, filename: str):
    """
    Play a score from a file given a set of parameters
    :param stream: PyAudio stream object
    :param filename: Name of the file containing the score string in the format "<note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>"
    :return: None
    """
    pass  # TODO: implement this function

if __name__ == "__main__":
    pass  # TODO: implement here
