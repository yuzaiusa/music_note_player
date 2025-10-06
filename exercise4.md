# Exercise 4: Transpose to a Different Key

Transposition is common practice in music. For example, to make a melody singing by female singers sung by a male singer, you usually need to transpose the moledy down by at least a perfect fourth or a perfect fifth, if not a whole octave. Transposition is to shift every note by the same distance. The distance is measured by how many half steps ($\frac{1}{12} of an octave).

We have two approaches to do this and we will try both.

## Exercise 4a Implement the transposition by transpose the score

The first approach is to transpose the score on the fly. If you want to transpose C major to Eb major, every notes need to be shift up by 3 half steps. C becomes Eb, C# becomes E, etc. This sounds like a map, right? The question is how to generate this map.

### Task 4.a

Make a class called `MusicNotePlayerV2a` derived from `MusicNotePlayerWithSave` in Exercise 3b. Override function `play_score` and `replay` to take another input parameter called `transpose` of type `int` and default value 0. The value of `transpose` could be positive or negative, meaning to shift every note up or down by that number half steps.

### Tip 4.a

The helper function `piano_note_frequencies` from Exercise 1b returns a dict that maps music notes to frequencies. The dict is not a good data structure to shift. You need something that is `indexed` by an integer. `List` is a natural choice.

## Exercise 4b Implement the transposition by shift the frequency

Another approach of transposition is to shift the frequency directly. Recall that the frequency of each note can be calculated using the formula:

$$ f(n) = 27.5 * 2^{\frac{n}{12}} $$

where $n$ is the number of half steps away from A0. To shift a given note up by m half steps, we have 

$$ f(n+m) = 27.5 * 2^{\frac{n+m}{12}} =  27.5 * 2^{\frac{n}{12}} * 2^{\frac{m}{12}} = f(n) * 2^{\frac{m}{12}} $$

So, it is easy to compute the shifted frequency using this formula.

### Task 4.b
Make a class called `MusicNotePlayerV2b` derived from `MusicNotePlayerWithSave` in Exercise 3b. Override function `play_note`, `play_score` and `replay` to take another input parameter called `transpose` of type `int` and default value 0. The value of `transpose` could be positive or negative, meaning to shift every note up or down by that number half steps.

### Tip 4.b
Only `play_note` needs to add new logic to handle the transposition. `play_score` and `replay` simply just need to pass the new parameter `transpose` through.
