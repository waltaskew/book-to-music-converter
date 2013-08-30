"""Grab gramatical features from the text."""


import itertools


SHIFT_SEGMENTS = 1.0 / 18.0
SHIFT_MAP = {
        0: 0, 1: 0, 2: 1, 3: -1, 4: 2, 5: -2, 6: 3, 7: -3, 8: 4, 9: -4,
        10: 5, 11: -5, 12: 6, 13: -6, 14: 7, 15: -7, 16: 8, 17: -8}


def iter_n_grams(text, n):
    """Return n-length pairs from the iterable text."""
    text = iter(text)
    n_grams = tuple(word for _, word in itertools.izip(xrange(n), text))
    while True:
        yield n_grams
        next_word = next(text)
        n_grams = n_grams[1:] + (next_word,)


def iter_pairs(iterable):
    """Iter by pairs through the iterable."""
    iterable = iter(iterable)
    first = next(iterable)
    second = next(iterable)
    while True:
        yield first, second
        first = second
        second = next(iterable)


def difference_as_pitch_shift(synset1, synset2):
    """Return the wordnet similarity of two synsets as a pitch shift."""
    similarity = synset1.path_similarity(synset2)
    as_shift = similarity // SHIFT_SEGMENTS
    return SHIFT_MAP[as_shift]


def iter_pitch_shifts(text, n, shift_func=difference_as_pitch_shift):
    """Return sequences of pitch shifts from an input text."""
    n_grams = iter_n_grams(text, n)

    prev_n_gram = next(n_grams)
    prev_shifts = (None,)
    prev_shifts += tuple(shift_func(synset1, synset2) for
            synset1, synset2 in iter_pairs(prev_n_gram))

    for n_gram in n_grams:
        new_shift = shift_func(prev_n_gram[-1], n_gram[-1])
        shifts = prev_shifts[1:] + (new_shift,)
        yield shifts
        prev_shifts = shifts
        prev_n_gram = n_gram


def record_shifts(shifts, prev_shift, cur_shift):
    """Add the sequence of pitch shifts to our history."""
    shift_map = shifts.setdefault(prev_shift, {})
    try:
        shift_map[cur_shift] += 1
    except KeyError:
        shift_map[cur_shift] = 1


def build_shift_map(text, n):
    """Build a dictionary counting the relative occurrence of
    pitch shifts.
    """
    shifts = {}
    for prev_shift, cur_shift in iter_pairs(iter_pitch_shifts(text, n)):
        record_shifts(shifts, prev_shift, cur_shift)
    return shifts
