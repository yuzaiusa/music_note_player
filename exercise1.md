# Exercise 1

In exercise, we will focus on basic concepts in python such as **list**, **dict** and **function**.

## Exercise 1a

In this exercise, we will use three functions from the helper_functions module:
1. `start_play`: Start a playback stream with a given sample rate. You will always need a stream to play a sound.
1. `play_frequency`: Play a single frequency sound for a specified duration.
1. `stop_play`: Stop the playback stream. It is a good practice to stop the stream after you finish playing sounds.
Think about how to make these functions available in this code (hint: by `import`).

You need to **initialize** a *player* (`stream`) before you play any sound by running `start_play()` to get a stream object.
Then, you are free to play any sound you like to on that stream object.
By the end, you need to **destroy** the *player* (`stream`) by `stop_play(stream)`.

The goal is to play the first measure of Twinkle Twinkle Little Star, which consists of the following notes:
```
C4, C4, G4, G4, A4, A4, G4
```
(in C major). Note the last note should be played for twice as long as the others.

Then, play this tune in D major.

An example of playing a single note (A4, 440 Hz) for 1 second is provided below.
```
    stream = start_play(sample_rate=44100)
    # Play a frequency of 440 Hz (A4) for 1 second at full volume with sample rate of 44100 Hz
    play_frequency(stream, frequency=440.0, duration=1.0, sample_rate=44100, amplitude=1.0)
    stop_play(stream)
```