import numpy as np
import pyaudio
from typing import Dict, List, Optional, Union

def start_play(sample_rate: float = 44100):
    """
    :param sample_rate: samples per second (441000  is the common audio sample rate)
    """
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    # Open audio stream
    stream = p.open(format=pyaudio.paFloat32, # Use float32 format for audio data
                    channels=1,              # Mono audio
                    rate=sample_rate,
                    output=True)
    return stream

def play_frequency(stream, frequency: float, duration: float, sample_rate: int = 44100, volume: float = 1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate sine wave
    # The formula for a sine wave is A * sin(2 * pi * f * t)
    # where A is amplitude, f is frequency, and t is time
    sine_wave = volume * np.sin(2 * np.pi * frequency * t)
    stream.write(sine_wave.astype(np.float32).tobytes())

def stop_play(stream):
    stream.stop_stream()
    stream.close()