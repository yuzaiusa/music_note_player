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
2. Play Score: function, string operation, file operation
    1. Write a function to play a line of "sheet score"
    2. Write a function to play a "sheet score" from a file
3. Play in Realtime: class, keyboard callback
    1. Write a class to handle the stream and be able to build up a score piece by piece and replay later.
    2. (Optional) Derive a class from the class in the previous exercise to play based on keystrokes.
4. Play Harmonies (and Different Sounds): class member function, function objects
    1. Deep dive into the play_frequency function to upgrade it into a function that can take two frequencies simultaneously. Also, allow it to use a different wave function to achieve a different sound.
    2. Modify the score format to allow two voices and let the player function to be able to play it.
    3. Modify the class to adopt the upgraded score format.
5. Transpose to a different key: class member function, function objects
    1. Implement the transposition by transpose the score
    2. Implement the transposition by shift the frequency
6. (Optional): Visualize Real Insturment Sound: pyaudio stream, numpy/pandas, pyplot
