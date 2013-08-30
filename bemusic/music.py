"""Generate music."""


import random


NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NOTE_COUNT = len(NOTES)


class Note(object):
    """Cute class to let us do math with notes."""

    def __init__(self, pitch, octave, note_number=None):
        if note_number is None:
            note_number = NOTES.index(pitch)

        self.pitch = pitch
        self.octave = octave
        self.note_number = note_number

    def __add__(self, steps):
        """Return the note @steps steps away from this note."""
        note_number = self.note_number + steps
        if note_number >= NOTE_COUNT or note_number < 0:
            octave = self.octave + (note_number // NOTE_COUNT)
            note_number = note_number % NOTE_COUNT
        else:
            octave = self.octave

        return Note(NOTES[note_number], octave, note_number=note_number)

    def __sub__(self, steps):
        return self + -steps

    def __repr__(self):
        return "Note(%s, %s, %s)" % (
                self.pitch,
                self.octave,
                self.note_number)


def most_popular_shift(shift_freqs):
    """Given a dictionary of shift occurrences, find the shift with the
    most occurrences following any previous shift.
    """
    totals = {}
    for shifts in shift_freqs.itervalues():
        for shift, count in shifts.iteritems():
            try:
                totals[shift] += count
            except KeyError:
                totals[shift] = count
    most_freq = max((count, shift) for shift, count in totals.iteritems())
    return most_freq[-1]


def next_shift(shift_freqs, prev_shift, default_shift):
    """Take a path down our choice tree."""
    try:
        choices = shift_freqs[prev_shift]
    except IndexError:
        return default_shift

    total_counts = sum(choices.itervalues())

    ranges = []
    range_start = 0
    for choice, count in choices.iteritems():
        range_count = count + range_start
        ranges.append((choice, range_count))
        range_start = range_count

    decision = random.randint(0, total_counts)
    for choice, range_count in ranges:
        if decision <= range_count:
            return choice
    # this shouldn't happen
    return choice
