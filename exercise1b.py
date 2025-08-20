"""
Exercise 1b: Play by Note
In this exercise, your are provided with a function that generates a dictionary mapping piano note names to 
their corresponding frequencies in Hertz.

The Physics behind this is that the frequency of a note doubles with each octave increase. For example, it is
well known that A4 (the A above middle C) is 440 Hz, and A5 (one octave higher) is 880 Hz and A3 (an octave lower)
is 220 Hz. Then, each semitone (half step) represents a frequency change by the twelfth root of 2 which is 
approximately 1.05946.

The piano has 88 keys, ranging from A0 (the lowest note) to C8 (the highest note). The frequency of each note can 
be calculated using the formula:
    f(n) = 27.5 * (2 ** (n / 12))
where n is the number of half steps away from A0. For example, A0 is 0 half steps away from A0, A#0/Bb0 is 1 half 
step away, B0 is 2 half steps away, C1 is 3 half steps away, and so on.

We try to include both sharp (#) and flat (b) notations for the notes. For example, A#4 and Bb4 both refer to the
same pitch (approximately 466.16 Hz).

The function piano_note_frequencies should return a dictionary where the keys are note names (e.g., 'A4', 'C#5')
and the values are their corresponding frequencies rounded to two decimal places.

Your task is to implement the function play_note that takes four REQUIRED parameters: stream, note, lenghth and 
tempo. Then use this function to play the whole song of Twinkle Twinkle Little Star in D major.

You may notice that this function interface is a bit different from play_frequency. We don't mention smaple_rate and
amplitude. Those two are still important parameters, but we don't want to type in their values every time. 
Instead, we want to make these two parameters OPTIONAL. if not specified, we will use a default sample_rate of
44100 Hz (the common audio sample rate) and a default amplitude of 1.0 (full volume). The function interface below
still has the sample_rate and amplitude as required parameters, please modify the function to make them optional.

The length parameter is in beats, where 1.0 represents a quarter note, 0.5 represents an eighth note, and so on.
The tempo parameter is in beats per minute (BPM) for a quarter note. For example, a tempo of 60 BPM means that
a quarter note lasts for 1 second, while a tempo of 120 BPM means that a quarter note lasts for 0.5 seconds.
Figure out the formula to convert length and tempo to duration in seconds, and write it down as a comment in the code.

Remember to start the audio stream before playing any notes and stop it after you finish playing all the notes.

Also think about how to write the code in a way that it can be easily modified to play other songs or change the tempo.
You don't want to write the function to play_note again and again for each note. Think about using loops and data structures
to make your code more efficient and reusable.

(Optional) Bonus: you may have noticed that the notes you have played are stick together without any pauses. It doesn't
sound very musical. You can add a small pause between notes to make it sound more natural. The pause should not make each 
note's overall duration longer otherwise you will mess up the tempo. It should be "zeroing out" the tail of the note.
The pause could be a fixed value, but it could not be too long, otherwise it will "eat up" some quick notes completely
in a fast tempo. An alternative is to make the pause duration proportional to the length of the note. But it could be 
too long for a long note. A good compromise is to make the pause duration a small fraction of the note length, 
such as 0.1 * length, with a cap on the maximum pause duration, such as 0.5 seconds.

If you have time, you can implement this in the play_note function as two additional optional parameters:
- pause_fraction: a fraction of the note length to use as the pause duration (default 0.1)
- max_pause_duration: a maximum duration for the pause (default 0.5 seconds)
"""
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
def play_note(stream: pyaudio.Stream, note: str, length: float, tempo: int, sample_rate: int, amplitude: float):
    """
    Play a note given a set of parameters
    :param stream: PyAudio stream object
    :param note: Note to be played (e.g., 'C4', 'D#5', 'Bb3')
    :param length: Duration of the note in beats (e.g., 1.0 for a quarter note, 0.5 for an eighth note)
    :param tempo: Tempo in beats per minute (BPM) for a quarter note
    :param sample_rate: Samples per second (44100 is the default audio sample rate)
    :param amplitude: Amplitude of the sound wave (0.0 to 1.0), 1.0 is the default amplitude
    :return: None
    """
    pass  # TODO: implement this function

if __name__ == "__main__":
    pass  # TODO: implement here