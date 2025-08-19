import numpy as np
import pyaudio
from typing import Dict, List, Optional, Union

"""
Helper Functions for the Music Note Player Project
"""
def start_play(sample_rate: float = 44100) -> pyaudio.Stream:
    """
    :param sample_rate: samples per second (441000  is the common audio sample rate)
    """
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    # Open audio stream
    stream = p.open(format=pyaudio.paFloat32, # Use float32 format for audio data
                    channels=1,               # Mono audio
                    rate=sample_rate,         # Set up the sample rate
                    output=True)
    return stream

def play_frequency(stream: pyaudio.Stream, frequency: float, duration: float, sample_rate: int = 44100, ampitude: float = 1.0):
    """
    Play a sound given a set of parameters
    :param stream: PyAudio stream object
    :param frequency: Frequency of the sound in Hertz
    :param duration: Duration to play the sound in seconds
    :param sample_rate: Samples per second (44100 is the common audio sample rate)
    :param ampitude: Amplitude of the sound wave (0.0 to 1.0)
    :return: None
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate sine wave
    # The formula for a sine wave is A * sin(2 * pi * f * t)
    # where A is amplitude, f is frequency, and t is time
    sine_wave = ampitude * np.sin(2 * np.pi * frequency * t)
    stream.write(sine_wave.astype(np.float32).tobytes())

def stop_play(stream: pyaudio.Stream):
    """
    Stop and close the PyAudio stream
    :param stream: PyAudio stream object
    :return: None
    """
    p = stream._pyaudio
    p.terminate()
    stream.stop_stream()
    stream.close()