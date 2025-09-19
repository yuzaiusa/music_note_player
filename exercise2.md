# Exercise 2: Play Score

In this exercise, we will focus on function, string operation and file operation.

## Exercise 2a Play a score line
You have managed to play some notes in Exercise 1. Now, let's build on that to play a "sheet music" score.

Our simplied sheet music is a string that contains note names, their lengths, and the tempo. 

The format is as follows:
```
    <note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>
```
where each note is followed by its length in beats, and the notes are separated by commas.

For example, the first measure of Twinkle Twinkle Little Star in C major can be represented as:
```
    C4/1.0,C4/1.0,G4/1.0,G4/1.0,A4/1.0,A4/1.0,G4/2.0
```

### Task 2.a
Your task is to implement a function `play_score` that takes a PyAudio stream, a string representing the score, and a tempo in beats per minute (BPM). The function should parse the score string (hint: use the `split` function), convert it into note-length pairs, and then use the `play_note` function from exercise1b to play.

Remember to start the audio stream before playing any notes and stop it after you finish playing all the notes.

### Tip 2.a:
The focus of this exercise is to practice built-in string operations and function calls. You can find a comprehensive list of string operations in [this reference page](https://www.w3schools.com/python/python_ref_string.asp).

Useful functions for this exercise is split. For the following exercises, you will also need learn to use startswith, endswith, strip, join and replace.

## Exercise 2b Play a score sheet file
In **excercise 2a**, you implemented a function to play a line of sheet music given as a string.  Now, let's build on that to play the whole song by taking the score from a text file.

### Task 2.b
Your task is to implement a function `play_score_file` that takes a PyAudio stream and a filename.  The function should read the score from the file, parse it into a string that can be passed to the `play_score` function from **exercise2a**.

The format of the score file is as follows:
```
    title: <tile of the song>
    tempo: <tempo in beats per minute (BPM)>
    score: <score string in the format "<note1>/<length1>,<note2>/<length2>, ..., <noteN>/<lengthN>">
```

For example, a score file for the first measure of Twinkle Twinkle Little Star in C major might look like this:
```
    title: Twinkle Twinkle Little Star
    tempo: 120
    score: C4/1.0,C4/1.0,G4/1.0,G4/1.0,A4/1.0,A4/1.0,G4/2.0
```
You can find the score file `sample_score.txt` in the same directory as this exercise file.

Remember to open the file within a with statement to ensure it is properly closed after reading.

Remember to start the audio stream before playing any notes and stop it after you finish playing all the notes.

### Tip 2.b
Tips:
1. It is often a good practice to open a file within a `with` statement to ensure it is properly closed after reading.  The typical usage is like:
```
    with open(filename, "r") as file:
        # do everything you need with the file
```
2. String function `strip` can be useful to remove any leading or trailing whitespace characters from each line, or even any splitted part of a line when you don't expect any leading or trailing whitespace characters.
