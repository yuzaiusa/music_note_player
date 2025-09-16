import pyaudio
from typing import Dict, List, Optional, Union
from helper_functions import play_frequency, start_play, stop_play

def piano_note_frequencies(round_to: int = 2) -> Dict[str, float]:
    sharp = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    flat  = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

    note_freq = {}
    for i in range(88):                         # i = 0..87, A0..C8
        idx = i % 12
        octave = (i + 9) // 12                  # A0→0, C1→1, ..., C8→8
        name_sharp = f"{sharp[idx]}{octave}"
        name_flat  = f"{flat[idx]}{octave}"
        freq = 27.5 * (2 ** (i / 12))           # A0 = 27.5 Hz
        if round_to is not None:
            freq = round(freq, round_to)
        note_freq[name_sharp] = freq
        note_freq[name_flat]  = freq
    return note_freq

# TODO: make sample_rate and amplitude optional parameters with default values
def play_note(stream: pyaudio.Stream, note: str, length: float, tempo: int, sample_rate: int, amplitude: float, pause_fraction: float = 0.1, max_pause_duration: float = 0.5):
    """
    Play a note given a set of parameters
    :param stream: PyAudio stream object
    :param note: Note to be played (e.g., 'C4', 'D#5', 'Bb3')
    :param length: Duration of the note in beats (e.g., 1.0 for a quarter note, 0.5 for an eighth note)
    :param tempo: Tempo in beats per minute (BPM) for a quarter note
    :param sample_rate: Samples per second (44100 is the default audio sample rate)
    :param amplitude: Amplitude of the sound wave (0.0 to 1.0), 1.0 is the default amplitude
    :pause_fraction: a fraction of the note length to use as the pause duration (default 0.1)
    :max_pause_duration: a maximum duration for the pause (default 0.5 seconds)
    :return: None
    """
    pass  # TODO: implement this function

if __name__ == "__main__":
    pass  # TODO: implement here
