"""Extract words and useful word features from a text."""


import nltk
import nltk.tokenize as tokenize

from nltk.corpus import stopwords
from nltk.corpus import wordnet


NOUN_TAG = 'N'
STOP_WORDS = set(stopwords.words('english'))


def iter_nouns(text):
    """Given a text, return an iterator yielding all of the nouns'
    synsets in the text.
    """
    for sentence in tokenize.sent_tokenize(text):
        for tagged_word in nltk.pos_tag(tokenize.word_tokenize(sentence)):
            word, pos = tagged_word
            if pos == NOUN_TAG and tagged_word[0] not in STOP_WORDS:
                synset = get_synset(word)
                if synset is not None:
                    yield synset


def get_synset(word):
    """Get the most likely synset for the given noun."""
    synsets = wordnet.synsets(word, pos=wordnet.NOUN)
    if not synsets:
        morphs = wordnet.morphy(word, wordnet.NOUN)
        if not morphs:
            return None
        else:
            synsets = wordnet.synsets(morphs[0], pos=wordnet.NOUN)

    if synsets:
        return synsets[0]
    else:
        return None
