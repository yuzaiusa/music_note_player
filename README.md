# Music note player
This is a set of fun coding exercises for beginners of Python. Some background of music theory may help to understand the context. But that is not strictly required to finish this exercise.

You will need pyaudio to do these exercises. To install pyaudio, you need to install portaudio first.
```
brew install portaudio
```

Then install pyaudio:
```
pip install pyaudio
```

List of exercises:

1. Play Note: import, dict, list, function
    1. Learn to use library functions to play by frequency
    2. Write a function to play by notes
    3. Improve the play by notes function to allow rests and add a small pause between notes to make it sound better
2. Play Score: function, string operation, file operation
    1. Write a function to play a line of "sheet score"
    2. Write a function to play a "sheet score" from a file
3. Adding and removing scores: class, member variable, member method, json, keyboard callback
    1. Write a class to handle the stream and be able to build up a score piece by piece and replay later.
    2. Write a save function and a load function for the class to save/load the scores into/from a json file.
4. Transpose to a different key: class inheritance
    1. Implement the transposition by transpose the score
    2. Implement the transposition by shift the frequency
5. Play Harmonies (and Different Sounds): function objects, class inheritance
    1. Deep dive into the play_frequency function to upgrade it into a function that can take two frequencies simultaneously, name the function play_frequencies.
    2. Allow the new play_frequencies function to use a different wave function to achieve a different sound.
    3. Modify the score format to allow two voices and let the player function to be able to play it.
    4. Modify the class to adopt the upgraded score format.
6. Visualize Real Insturment Sound: wave, numpy/pandas, pyplot
    1. Visualize the sine_wave and box_wave that was made in exercise 5b
    2. Use wave to load a sample piano note. Visualize its wave.
    3. Based on the sound you recorded, manipulate their frequencies to make the sound in a different pitch
    4. Make your music player to use this naive instrument sound
