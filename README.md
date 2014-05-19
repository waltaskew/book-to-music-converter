Books To Music
==============
Convert your favorite text files into MIDI goodness!

Wait, What?
-----------
Sure, you've read The Brother's Karamazov, but have you ever heard it?
Have your ears enjoyed the sweet trills of Alyosha or the sardonic
etudes of Ivan?
This innovative software allows you to convert text into music, with
the latest in natural language processing and MIDI technology!

Wait, How?
----------
Given some text, the program builds a probabilistic model describing
shifts in the deltas of lexical distances between consecutive words.
These probabilities describing lexical distance deltas are then
re-interpreted as deltas between pitches, allowing us to use this
probabilistic model to generate random pieces of music.

So, is the result of this at all meaningful?
--------------------------------------------
Not really, but I am glad to live in the sort of world where this kind
of thing can exist.

Natural Language Processing 101
-------------------------------
We use the excellent NLP resource Wordnet to determine lexical
distances between words.
"Lexical distance" is a measure of semantic nearness between words --
"dog" and "cat" are closer together than "dog" and "rock" but further
apart than "dog" and "hound."
Using Wordnet, we can build sequences of lexical distances between
consecutive words, and given these sequences we can build a
probabilistic state machine which tells us the likelihood of a given
lexical distance between the next two words given the lexical distance
between the previous two words.

We can extend this notion a bit to deal with n-grams of words rather
than single words.
For example if we chose to take 2-grams (bigrams) to build our model,
then given the lexical distances between the previous three words,
our model predicts the delta most likely to follow the pair of deltas
between those three words.
We can take this out to groups of n size, simulating some understanding
of context in our probabilistic model.

Requirements
------------
https://code.google.com/p/midiutil/

http://www.nltk.org

You'll need to use the nltk.dowload utility to grab the NLTK corpora
and models to use the library.
You'll need the stop words and wordnet corpora and the punkt and treebank
models,
but go ahead and download them all -- nltk is a great library!

```
$ python
>>> import nltk
>>> nltk.download()
```

Usage
-----
The 'bemusic' script in the 'bemusic' directory is the entry point for usage.

```
$ cd bemusic
$ ./bemusic -h

usage: bemusic [-h] [-s SONG_LENGTH] [-n N_GRAM_LENGTH] input_file

Convert a text file into a midi using NLP tom-foolery. Creates a new file
named after the input file in the current directory.

positional arguments:
  input_file            text file to convert to a midi

optional arguments:
  -h, --help            show this help message and exit
  -s SONG_LENGTH, --song-length SONG_LENGTH
                        how many beats long the output midi will be, defaults
                        to 300
  -n N_GRAM_LENGTH, --n-gram-length N_GRAM_LENGTH
                        The size of the n-grams to be used when building a
                        grammar, defaults to bigrams
```
The script produces a MIDI file with the same name as the text file given
to the script.
You can then use your favorite MIDI player to listen to your book!